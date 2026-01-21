from pathlib import Path
import json

from rag.ingest.loaders import load_pdf
from rag.ingest.normalize import normalize_text

RAW_DIR = Path("data/raw")
OUTPUT = Path("reports/ingest_sample.jsonl")

def main():
    all_docs = []

    for pdf in RAW_DIR.glob("*.pdf"):
        docs = load_pdf(pdf)
        for d in docs:
            d.text = normalize_text(d.text)
            all_docs.append(d)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        for doc in all_docs:
            record = {
                "text": doc.text,
                "metadata": doc.metadata
            }
            f.write(json.dumps(record) + "\n")

    num_files = len(list(RAW_DIR.glob("*.pdf")))
    num_pages = len(all_docs)
    print(f"Ingested {num_files} documents")
    print(f"Extrated {num_pages} pages")

if __name__ == "__main__":
    main()
