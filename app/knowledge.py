"""
Knowledge base for the Aspire Cloud bot.

Search strategy
---------------
We use BM25, the standard ranking function used by search engines and
libraries like Elasticsearch. Unlike naive keyword counting, BM25:

  * Down-weights words that appear in many chunks (e.g. "work", "ticket")
    via inverse document frequency (IDF). Rare, distinctive words score higher.
  * Saturates term frequency, so a chunk that repeats a word 50 times does
    not dominate one that uses it 3 times in a focused way.
  * Normalizes by chunk length, so long chunks don't win just by being big.

On top of BM25 we add light domain logic:
  * Multi-word Aspire terms ("work order", "fixed payment") are scored as a
    unit, because the individual words are nearly useless on their own.
  * The chunk's source filename and header line get a relevance boost,
    because "how do I cancel a work ticket" should favor the worktickets doc.

Chunking strategy
-----------------
Markdown is split on H2 (##). Any H2 section longer than MAX_CHUNK_CHARS is
further split on H3 (###) so that focused topics (e.g. "Contracts" vs
"Work Orders" under "Opportunity Types") become their own retrievable units.
Every chunk is prefixed with "<source> > <header>" so the model always knows
where the text came from.

No external dependencies — BM25 is implemented here so deployment stays simple.
"""

import math
import re
from pathlib import Path


# Words ignored when building the query term list. Kept deliberately small —
# BM25's IDF already handles common words; this just removes question framing.
STOP_WORDS = {
    "how", "do", "i", "a", "an", "the", "is", "are", "was", "were", "be",
    "to", "in", "of", "and", "or", "for", "on", "it", "can", "could", "my",
    "me", "this", "that", "with", "from", "what", "when", "where", "why",
    "which", "who", "you", "your", "we", "our", "if", "but", "not", "no",
    "does", "did", "will", "would", "should", "may", "might", "about",
    "between", "difference", "explain", "tell", "describe", "vs", "versus",
    "there", "their", "they", "its", "so", "up", "out", "just", "also",
    "need", "want", "get", "set", "use", "using", "make",
}

# Multi-word Aspire terms. When the query contains one of these, we match it
# as a phrase against chunks. Order doesn't matter; longer phrases first so
# "fixed price open billing" is tried before "fixed price".
ASPIRE_PHRASES = [
    "fixed price open billing", "fixed price on payment schedule",
    "fixed price on completion", "time and materials", "schedule of values",
    "dynamic forecasting", "fixed payment", "per service", "work ticket",
    "work order", "change order", "credit memo", "payment schedule",
    "schedule board", "contract renewal", "invoice type", "billing type",
    "opportunity type", "service visit", "bulk action", "purchase receipt",
    "weekly time review", "time entry", "as needed", "general conditions",
    "job dashboard", "electronic payment", "fixed price", "open billing",
    "t&m", "fpob", "sov",
]

# Tuning constants for BM25
BM25_K1 = 1.5   # term-frequency saturation point
BM25_B = 0.75   # length-normalization strength

# Header keywords that signal a section DEFINES or gives an OVERVIEW of terms.
# Used to boost such sections for conceptual ("what is", "difference") queries.
DEFINITIONAL_HEADERS = (
    "concept", "type", "what is", "what are", "overview", "key ",
    "terminology", "introduction", "difference", "vs",
)

# Phrases in a query that signal the user wants a definition or comparison
# rather than a procedure.
CONCEPTUAL_QUERY_MARKERS = (
    "difference", "differ", "what is", "what are", "vs", "versus",
    "compare", "comparison", "explain", "meaning", "definition",
    "define", "type of", "types of", "when to use", "when do i use",
)

# Chunking
# Adaptive retrieval: keep chunks scoring at least this fraction of the
# top chunk's score. Lower = more chunks kept. 0.35 trims weak matches.
RELATIVE_CUTOFF = 0.35

MAX_CHUNK_CHARS = 1800   # H2 sections longer than this get split on H3
MIN_CHUNK_CHARS = 40     # ignore tiny fragments


def _stem(word: str) -> str:
    """Very lightweight suffix stemmer so 'contracts'->'contract',
    'orders'->'order', 'invoicing'->'invoic', 'scheduled'->'schedul'.
    Not linguistically perfect, but it makes singular/plural and common
    verb forms match, which is what matters for retrieval. Deliberately
    conservative to avoid collapsing unrelated words."""
    if len(word) <= 3:
        return word
    for suffix in ("ies", "ing", "ed", "es", "s"):
        if word.endswith(suffix) and len(word) - len(suffix) >= 3:
            if suffix == "ies":
                return word[:-3] + "y"
            return word[: -len(suffix)]
    return word


def _tokenize(text: str) -> list:
    """Lowercase word tokenizer with stemming. Keeps alphanumerics and a few
    symbols that matter in Aspire (& for T&M, % for percentages)."""
    raw = re.findall(r"[a-z0-9&%]+", text.lower())
    return [_stem(t) for t in raw]


class KnowledgeBase:
    def __init__(self, docs_dir: str = "docs"):
        self.chunks = []          # list of dicts: source, header, content, text
        self._doc_tokens = []     # tokenized chunk text, parallel to self.chunks
        self._doc_freqs = []      # term -> count per chunk
        self._idf = {}            # term -> idf weight
        self._avg_len = 0.0
        self._load(docs_dir)
        self._build_index()

    # ----- loading & chunking -------------------------------------------------

    def _load(self, docs_dir: str):
        docs_path = Path(docs_dir)
        if not docs_path.exists():
            print(f"WARNING: '{docs_dir}/' not found — knowledge base is empty")
            return

        files = sorted(docs_path.glob("*.md"))
        for md_file in files:
            try:
                content = md_file.read_text(encoding="utf-8")
            except Exception as e:
                print(f"ERROR reading {md_file.name}: {e}")
                continue
            self._chunk_file(md_file.stem, content)

        print(f"Loaded {len(self.chunks)} chunks from {len(files)} files")

    def _chunk_file(self, source: str, content: str):
        # Split on H2
        h2_parts = re.split(r"\n(?=## )", content)
        for part in h2_parts:
            part = part.strip()
            if len(part) < MIN_CHUNK_CHARS:
                continue

            header = part.split("\n", 1)[0].lstrip("#").strip()

            if len(part) <= MAX_CHUNK_CHARS:
                self._add_chunk(source, header, part)
            else:
                # Split big sections on H3 to isolate sub-topics
                h3_parts = re.split(r"\n(?=### )", part)
                if len(h3_parts) == 1:
                    # No H3s; keep whole (better than dropping)
                    self._add_chunk(source, header, part)
                else:
                    for sub in h3_parts:
                        sub = sub.strip()
                        if len(sub) < MIN_CHUNK_CHARS:
                            continue
                        sub_header = sub.split("\n", 1)[0].lstrip("#").strip()
                        full_header = (
                            header if sub_header == header
                            else f"{header} > {sub_header}"
                        )
                        self._add_chunk(source, full_header, sub)

    def _add_chunk(self, source: str, header: str, content: str):
        # Prefix gives the model provenance and adds searchable context
        prefix = f"[{source.replace('_', ' ')}] {header}"
        self.chunks.append({
            "source": source,
            "header": header,
            "content": content,
            "text": f"{prefix}\n{content}",
        })

    # ----- BM25 index ---------------------------------------------------------

    def _build_index(self):
        if not self.chunks:
            return

        total_len = 0
        df = {}  # document frequency: term -> # chunks containing it

        for chunk in self.chunks:
            tokens = _tokenize(chunk["text"])
            self._doc_tokens.append(tokens)
            total_len += len(tokens)

            freqs = {}
            for t in tokens:
                freqs[t] = freqs.get(t, 0) + 1
            self._doc_freqs.append(freqs)

            for t in freqs:
                df[t] = df.get(t, 0) + 1

        n = len(self.chunks)
        self._avg_len = total_len / n if n else 0.0

        # BM25 idf with +1 smoothing so it never goes negative
        for term, freq in df.items():
            self._idf[term] = math.log(1 + (n - freq + 0.5) / (freq + 0.5))

    # ----- query --------------------------------------------------------------

    def _query_terms(self, query: str):
        q_lower = query.lower()

        phrases = [p for p in ASPIRE_PHRASES if p in q_lower]

        words = [
            w for w in _tokenize(query)
            if w not in STOP_WORDS and len(w) > 1
        ]
        # Fallback: if stop-word removal nuked everything, keep raw tokens
        if not words and not phrases:
            words = _tokenize(query)

        return words, phrases

    def _bm25_score(self, idx: int, terms: list) -> float:
        freqs = self._doc_freqs[idx]
        dl = len(self._doc_tokens[idx])
        score = 0.0
        for term in terms:
            tf = freqs.get(term, 0)
            if tf == 0:
                continue
            idf = self._idf.get(term, 0.0)
            denom = tf + BM25_K1 * (1 - BM25_B + BM25_B * dl / self._avg_len)
            score += idf * (tf * (BM25_K1 + 1)) / denom
        return score

    def search(self, query: str, top_k: int = 6) -> list:
        if not self.chunks:
            return []

        words, phrases = self._query_terms(query)
        q_lower = query.lower()

        # Is this a "define / compare" question vs a "how do I" procedure?
        is_conceptual = any(m in q_lower for m in CONCEPTUAL_QUERY_MARKERS)

        # Stem the phrases too, so "work order" matches "work orders" in text.
        # We match phrases against a stemmed version of each chunk's tokens
        # joined back into a string.
        stemmed_phrases = [" ".join(_tokenize(p)) for p in phrases]

        # Build the set of distinct "concepts" the query is about. A concept
        # is either an Aspire phrase or a content keyword. Comparison questions
        # ("difference between X and Y") want a chunk that covers BOTH, so we
        # reward breadth of coverage, not just depth on one term.
        concepts = list(stemmed_phrases)
        phrase_words = {w for p in stemmed_phrases for w in p.split()}
        concepts += [w for w in words if w not in phrase_words]
        concepts = list(dict.fromkeys(concepts))  # dedupe, keep order

        scored = []
        for idx, chunk in enumerate(self.chunks):
            score = self._bm25_score(idx, words)

            # Stemmed text for phrase/coverage matching
            stemmed_text = " ".join(self._doc_tokens[idx])
            header_lower = chunk["header"].lower()
            stemmed_header = " ".join(_tokenize(chunk["header"]))
            source_lower = chunk["source"].lower().replace("_", " ")

            # Phrase matches are strong signals (the words alone are weak)
            for phrase in stemmed_phrases:
                if phrase in stemmed_text:
                    score += 6.0
                if phrase in stemmed_header:
                    score += 4.0  # phrase in the header = very on-topic

            # Coverage boost: how many of the distinct query concepts does this
            # chunk contain at all? A chunk covering 3/3 concepts is far more
            # likely to answer a comparison than one covering 1/3 very densely.
            if concepts:
                covered = sum(1 for c in concepts if c in stemmed_text)
                coverage_ratio = covered / len(concepts)
                score += 8.0 * (coverage_ratio ** 2)
                if covered == len(concepts) and len(concepts) >= 2:
                    score += 5.0

            # Definitional boost: questions like "what is X" or
            # "difference between X and Y" are best answered by sections that
            # DEFINE things. Reward chunks whose header signals a definition
            # or overview, when the query is conceptual.
            if is_conceptual:
                if any(kw in header_lower for kw in DEFINITIONAL_HEADERS):
                    score += 7.0
                # The compact concept/overview chunks are ideal here
                if "concept" in header_lower or "type" in header_lower:
                    score += 3.0

            # Header / source relevance boosts
            for w in words:
                if w in stemmed_header:
                    score += 1.5
                if w in source_lower:
                    score += 1.0

            if score > 0:
                scored.append((score, chunk))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [c for _, c in scored[:top_k]]


    def search_scored(self, query: str, top_k: int = 6):
        """Like search() but also returns diagnostic scores used for
        relevance gating and adaptive chunk count.

        Returns a dict:
          chunks: list of chunk dicts (after adaptive trimming)
          max_pure_bm25: highest pure BM25 score (0 = no content match at all)
          max_total: highest combined score (with boosts)
        Pure BM25 == 0 is a reliable 'off-topic / not in KB' signal because
        off-topic questions share no content words with any chunk.
        """
        if not self.chunks:
            return {"chunks": [], "max_pure_bm25": 0.0, "max_total": 0.0}

        words, phrases = self._query_terms(query)
        q_lower = query.lower()
        is_conceptual = any(m in q_lower for m in CONCEPTUAL_QUERY_MARKERS)

        stemmed_phrases = [" ".join(_tokenize(p)) for p in phrases]
        concepts = list(stemmed_phrases)
        phrase_words = {w for p in stemmed_phrases for w in p.split()}
        concepts += [w for w in words if w not in phrase_words]
        concepts = list(dict.fromkeys(concepts))

        max_pure = 0.0
        scored = []
        for idx, chunk in enumerate(self.chunks):
            pure = self._bm25_score(idx, words)
            if pure > max_pure:
                max_pure = pure
            score = pure

            stemmed_text = " ".join(self._doc_tokens[idx])
            header_lower = chunk["header"].lower()
            stemmed_header = " ".join(_tokenize(chunk["header"]))
            source_lower = chunk["source"].lower().replace("_", " ")

            for phrase in stemmed_phrases:
                if phrase in stemmed_text:
                    score += 6.0
                if phrase in stemmed_header:
                    score += 4.0

            if concepts:
                covered = sum(1 for c in concepts if c in stemmed_text)
                cov = covered / len(concepts)
                score += 8.0 * (cov ** 2)
                if covered == len(concepts) and len(concepts) >= 2:
                    score += 5.0

            if is_conceptual:
                if any(kw in header_lower for kw in DEFINITIONAL_HEADERS):
                    score += 7.0
                if "concept" in header_lower or "type" in header_lower:
                    score += 3.0

            for w in words:
                if w in stemmed_header:
                    score += 1.5
                if w in source_lower:
                    score += 1.0

            if score > 0:
                scored.append((score, chunk))

        scored.sort(key=lambda x: x[0], reverse=True)
        top = scored[:top_k]
        max_total = top[0][0] if top else 0.0

        # Adaptive trimming: keep chunks whose score is at least
        # RELATIVE_CUTOFF of the best chunk. Simple questions naturally
        # end up with fewer chunks; complex ones keep more.
        if top:
            best = top[0][0]
            kept = [c for s, c in top if s >= best * RELATIVE_CUTOFF]
        else:
            kept = []

        return {
            "chunks": kept,
            "max_pure_bm25": round(max_pure, 2),
            "max_total": round(max_total, 2),
        }

    # ----- diagnostics --------------------------------------------------------

    def stats(self) -> dict:
        return {
            "total_chunks": len(self.chunks),
            "sources": sorted({c["source"] for c in self.chunks}),
            "avg_chunk_tokens": round(self._avg_len, 1),
            "vocab_size": len(self._idf),
        }
