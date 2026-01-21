import chromadb
from pathlib import Path
from typing import List, Dict

class VectorStore:
    """Handles the storage and retrieval of vector embeddings using ChromaDB."""
    
    def __init__(self, db_path: str = "storage/chroma_db"):
        # Ensure the directory exists
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        
        self.client = chromadb.PersistentClient(path=db_path)
        self.collection = self.client.get_or_create_collection(
            name="rag_collection",
            metadata={"hnsw:space": "cosine"} # Using cosine similarity
        )

    def upsert_chunks(self, chunks: List[Dict], embeddings: List[List[float]]):
        """Insert or update chunks and their embeddings in the database."""
        ids = [c["chunk_id"] for c in chunks]
        documents = [c["text"] for c in chunks]
        metadatas = [c["metadata"] for c in chunks]

        self.collection.upsert(
            ids=ids,
            embeddings=embeddings,
            metadatas=metadatas,
            documents=documents
        )