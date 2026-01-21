from dataclasses import dataclass, asdict
from typing import Dict, List
import uuid

@dataclass
class Chunk:
    chunk_id: str
    text: str
    metadata: Dict[str, str]

def split_text(text: str, chunk_size: int = 800, overlap: int = 100) -> List[str]:
    chunks = []
    start = 0

    if overlap >= chunk_size:
        overlap = chunk_size // 2

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap

        if end >= len(text):
            break
    return chunks

def create_chunks(record: dict, chunk_size=800, overlap=100):
    text = record.get("text", "")
    metadata = record.get("metadata", {})
    
    texts = split_text(text, chunk_size, overlap)
    chunks = []

    for idx, t in enumerate(texts):
        chunk_obj = Chunk(
            chunk_id=str(uuid.uuid4()),
            text=t,
            metadata={
                **metadata,
                "chunk_index": idx
            }
        )
        chunks.append(asdict(chunk_obj)) 

    return chunks