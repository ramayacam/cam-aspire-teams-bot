from pathlib import Path
import re


# Common words to ignore in search
STOP_WORDS = {
    "how", "do", "i", "a", "the", "is", "what", "to", "in", "of",
    "and", "or", "for", "on", "it", "can", "my", "me", "this",
    "that", "an", "be", "are", "was", "were", "been", "have", "has",
    "had", "will", "would", "could", "should", "may", "might",
    "does", "did", "about", "with", "from", "when", "where", "why",
    "which", "who", "whom", "there", "their", "they", "you", "your",
    "we", "our", "its", "if", "but", "not", "no", "all", "any",
    "each", "than", "then", "so", "up", "out", "just", "also",
}


class KnowledgeBase:
    """Loads markdown docs and searches by keyword matching."""

    def __init__(self):
        self.chunks = []
        self._load_documents()

    def _load_documents(self):
        docs_path = Path("docs")
        if not docs_path.exists():
            print("Warning: docs/ folder not found")
            return

        for md_file in sorted(docs_path.glob("*.md")):
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()

            sections = content.split("\n## ")
            for i, section in enumerate(sections):
                if i > 0:
                    section = "## " + section
                if len(section.strip()) > 50:
                    self.chunks.append({
                        "source": md_file.stem,
                        "content": section.strip()
                    })

        print(f"Loaded {len(self.chunks)} chunks from {docs_path}")

    def search(self, query: str, top_k: int = 5) -> list:
        """Keyword search with stop word filtering and phrase matching."""
        query_lower = query.lower()
        query_words = {
            w for w in re.findall(r'\w+', query_lower)
            if w not in STOP_WORDS and len(w) > 2
        }

        if not query_words:
            query_words = set(re.findall(r'\w+', query_lower))

        scored = []

        for chunk in self.chunks:
            chunk_lower = chunk["content"].lower()
            score = 0

            # Exact phrase bonus (big boost)
            for phrase_len in [3, 2]:
                words = list(query_words)
                for j in range(len(words) - phrase_len + 1):
                    phrase = " ".join(words[j:j + phrase_len])
                    if phrase in chunk_lower:
                        score += 10 * phrase_len

            # Individual keyword matches
            for word in query_words:
                count = chunk_lower.count(word)
                if count > 0:
                    score += count

            # Title/header bonus
            first_line = chunk_lower.split("\n")[0]
            for word in query_words:
                if word in first_line:
                    score += 5

            if score > 0:
                scored.append((score, chunk))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [item[1] for item in scored[:top_k]]
