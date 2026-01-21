import json
from pathlib import Path
from rag.chunking.splitters import create_chunks

INPUT = Path("reports/ingest_sample.jsonl")
OUTPUT = Path("reports/chunks.jsonl") 

def main():
    total_chunks = 0
    lengths = []
    all_chunks = []

    if not INPUT.exists():
        print(f"Error: No files found {INPUT}")
        return

    with open(INPUT, encoding="utf-8") as f:
        for line in f:
            record = json.loads(line)
            chunks = create_chunks(record) 
            
            total_chunks += len(chunks)
            lengths.extend([len(c['text']) for c in chunks])
            all_chunks.extend(chunks)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        for chunk in all_chunks:
            f.write(json.dumps(chunk) + "\n")

    print(f"✅ Process complete")
    print(f"Total chunks: {total_chunks}")
    if lengths:
        print(f"Mean Characters per chunk: {sum(lengths) / len(lengths):.1f}")

if __name__ == "__main__":
    main()