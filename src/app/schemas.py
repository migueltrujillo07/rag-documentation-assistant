from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class IngestRequest(BaseModel):
    path: Optional[str] = None  # default: settings.docs_dir

class QueryRequest(BaseModel):
    question: str
    top_k: Optional[int] = None
    filters: Optional[Dict[str, Any]] = None

class Source(BaseModel):
    source: str
    section: Optional[str] = None
    chunk_id: str

class QueryResponse(BaseModel):
    answer: str
    sources: List[Source]
