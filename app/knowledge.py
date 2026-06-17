from pathlib import Path


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
        query_words = set(query.lower().split())
        scored = []

        for chunk in self.chunks:
            chunk_lower = chunk["content"].lower()
            score = sum(1 for word in query_words if word in chunk_lower)
            if score > 0:
                scored.append((score, chunk))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [item[1] for item in scored[:top_k]]
