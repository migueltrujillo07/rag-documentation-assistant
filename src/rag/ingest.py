from pathlib import Path
from typing import List
from langchain_core.documents import Document

def load_markdown_dir(docs_dir: str) -> List[Document]:
    docs: List[Document] = []
    root = Path(docs_dir)
    for path in root.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        docs.append(
            Document(
                page_content=text,
                metadata={
                    "source": str(path.as_posix()),
                    "doc_title": path.stem,
                    "content_type": "markdown",
                },
            )
        )
    return docs
