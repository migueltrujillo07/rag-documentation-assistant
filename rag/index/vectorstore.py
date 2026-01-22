import chromadb
from pathlib import Path
from typing import List, Dict

class VectorStore:
    def __init__(self, db_path: str = "storage/chroma_db"):
        self.client = chromadb.PersistentClient(path=db_path)
        self.collection = self.client.get_or_create_collection(name="rag_collection")

    def upsert_chunks(self, chunks: List[Dict], embeddings: List[List[float]]):
        ids = [c["chunk_id"] for c in chunks]
        documents = [c["text"] for c in chunks]
        metadatas = [c["metadata"] for c in chunks]
        self.collection.upsert(ids=ids, embeddings=embeddings, metadatas=metadatas, documents=documents)

    # ADD THIS METHOD:
    def search(self, query_embedding: List[float], n_results: int = 3):
        """Retrieve the most similar chunks based on vector distance."""
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )