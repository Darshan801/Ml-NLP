from sentence_transformers import  CrossEncoder
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def retrieve(query, index, chunks, embed_model, top_k=12, final_k=3):
    # Dense retrieval
    query_embedding = embed_model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    )
    distances, indices = index.search(query_embedding, top_k)
    candidates = [chunks[i] for i in indices[0]]

    # Re-ranking
    pairs = [(query, chunk) for chunk in candidates]
    rerank_scores = reranker.predict(pairs)
    ranked = sorted(
        zip(candidates, rerank_scores),
        key=lambda x: x[1],
        reverse=True
    )
    top_chunks = [chunk for chunk, _ in ranked[:final_k]]

    return "\n\n".join(top_chunks)