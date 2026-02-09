from sentence_transformers import SentenceTransformer , cross_encoder
import faiss
import numpy as np

EMBEDDING_MODEL = SentenceTransformer("all-MiniLM-L6-v2")

# faiss stores embeddings and enables semantic search
def create_vector_store(chunks):
    embeddings = EMBEDDING_MODEL.encode(chunks)
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    return index , chunks