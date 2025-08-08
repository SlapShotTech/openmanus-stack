from typing import List
import numpy as np
import uuid


class SimpleRAG:
    """A minimal retrieval augmented generation interface.

    This stub stores embeddings in memory for demonstration.  In production,
    use pgvector with sentence-transformers.
    """

    def __init__(self) -> None:
        self.store: dict[str, np.ndarray] = {}
        self.texts: dict[str, str] = {}

    def add(self, text: str, embedding: np.ndarray) -> str:
        doc_id = str(uuid.uuid4())
        self.store[doc_id] = embedding
        self.texts[doc_id] = text
        return doc_id

    def search(self, query_embedding: np.ndarray, top_k: int = 3) -> List[str]:
        scores = []
        for doc_id, emb in self.store.items():
            score = float(np.dot(query_embedding, emb) / (np.linalg.norm(query_embedding) * np.linalg.norm(emb)))
            scores.append((score, doc_id))
        scores.sort(reverse=True)
        return [self.texts[doc_id] for _, doc_id in scores[:top_k]]