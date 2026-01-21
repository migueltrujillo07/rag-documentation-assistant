# rag/ingest/loaders.py
from dataclasses import dataclass
from typing import Dict

@dataclass
class Document:
    text: str
    metadata: Dict[str, str]

from pathlib import Path
from PyPDF2 import PdfReader

def load_pdf(path: Path) -> list[Document]:
    reader = PdfReader(path)
    documents = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if not text:
            continue

        documents.append(
            Document(
                text=text,
                metadata={
                    "source": path.name,
                    "page": str(i + 1),
                    "type": "pdf"
                }
            )
        )

    return documents
