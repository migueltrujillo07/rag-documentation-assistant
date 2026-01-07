from pydantic import BaseSettings

class Settings(BaseSettings):
    chroma_persist_dir: str = "./data/chroma"
    docs_dir: str = "./data/raw_docs"
    top_k: int = 6
    ollama_base_url: str = "http://localhost:11434"

    class Config:
        env_file = ".env"

settings = Settings()