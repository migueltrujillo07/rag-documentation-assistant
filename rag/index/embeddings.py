import ollama
from typing import List

class EmbeddingManager:
    """Manages text-to-vector conversions using Ollama."""
    
    def __init__(self, model_name: str = "nomic-embed-text"):
        self.model_name = model_name

    def get_embeddings(self, text: str) -> List[float]:
        """Convert a single string into an embedding vector."""
        response = ollama.embeddings(model=self.model_name, prompt=text)
        return response["embedding"]

    def create_batches(self, items: list, batch_size: int):
            """Helper to split a list into smaller batches."""
            for i in range(0, len(items), batch_size):
                yield items[i : i + batch_size]