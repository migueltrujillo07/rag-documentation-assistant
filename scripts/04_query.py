import sys
from rag.index.embeddings import EmbeddingManager
from rag.index.vectorstore import VectorStore

def main():
    # 1. Initialize tools
    embedder = EmbeddingManager()
    store = VectorStore()
    
    # 2. Get query from user
    if len(sys.argv) > 1:
        query_text = " ".join(sys.argv[1:])
    else:
        query_text = input("Enter your search query: ")

    print(f"\nSearching for: '{query_text}'...")

    # 3. Convert query to vector
    query_vector = embedder.get_embeddings(query_text)

    # 4. Search in ChromaDB
    # We ask for the top 3 most relevant chunks
    results = store.search(query_vector, n_results=3)

    # 5. Display results (Validation)
    print("\n" + "="*50)
    print("TOP RELEVANT CHUNKS FOUND:")
    print("="*50)

    for i in range(len(results['ids'][0])):
        content = results['documents'][0][i]
        metadata = results['metadatas'][0][i]
        distance = results['distances'][0][i] # Smaller means more similar
        
        print(f"\n[Result {i+1}] (Distance: {distance:.4f})")
        print(f"Source: {metadata.get('source')} - Page: {metadata.get('page')}")
        print(f"Content snippet: {content[:200]}...")
        print("-" * 30)

if __name__ == "__main__":
    main()