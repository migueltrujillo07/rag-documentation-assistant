import json
from pathlib import Path
from rag.index.embeddings import EmbeddingManager
from rag.index.vectorstore import VectorStore

# Configuration
INPUT_CHUNKS = Path("reports/chunks.jsonl")
BATCH_SIZE = 50  # Number of chunks to process at once

def main():
    if not INPUT_CHUNKS.exists():
        print(f"Error: {INPUT_CHUNKS} not found.")
        return

    embedder = EmbeddingManager()
    store = VectorStore()
    
    # Load all chunks into memory (since 313 chunks is small)
    all_chunks = []
    with open(INPUT_CHUNKS, "r", encoding="utf-8") as f:
        for line in f:
            all_chunks.append(json.loads(line))
    
    print(f"Total chunks to index: {len(all_chunks)}")
    print(f"Processing in batches of {BATCH_SIZE}...")

    # Iterate through batches
    for i, batch in enumerate(embedder.create_batches(all_chunks, BATCH_SIZE)):
        # Extract text from the current batch
        batch_texts = [c["text"] for c in batch]
        
        # Generate embeddings for the batch
        # Note: We do this sequentially to keep it simple for local Ollama
        batch_embeddings = [embedder.get_embeddings(t) for t in batch_texts]
        
        # Upsert the batch into ChromaDB
        store.upsert_chunks(batch, batch_embeddings)
        
        processed_count = min((i + 1) * BATCH_SIZE, len(all_chunks))
        print(f"Progress: {processed_count}/{len(all_chunks)} chunks indexed.")

    print(f"✅ Successfully indexed all chunks in storage/chroma_db")

if __name__ == "__main__":
    main()