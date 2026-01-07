from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(
    docs: List[Document],
    chunk_size: int = 900,
    chunk_overlap: int = 150,
) -> List[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n## ", "\n### ", "\n#### ", "\n", " ", ""],
    )
    chunks = splitter.split_documents(docs)

    # Add stable-ish chunk ids
    for i, d in enumerate(chunks):
        d.metadata["chunk_index"] = i
        d.metadata["chunk_id"] = f'{d.metadata.get("source","unknown")}::chunk::{i}'
    return chunks
