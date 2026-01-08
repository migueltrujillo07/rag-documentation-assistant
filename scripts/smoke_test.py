import os 
from dotenv import load_dotenv
import faiss
import numpy as np

load_dotenv()

def test_env():
    print("LLM PROVIDER: ", os.getenv("LLM_PROVIDER"))
    print("EMBEDDING MODEL: ", os.getenv("EMBEDDING_MODEL"))

def test_faiss():
    dim = 8
    index = faiss.IndexFlatL2(dim)
    x = np.random.rand(5,dim).astype("float32")
    index.add(x)
    D, I = index.search(x[:1], k=3)
    print("FAISS OK: ", D, I)

if __name__ == "__main__":
    test_env()
    test_faiss()