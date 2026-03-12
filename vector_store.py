import numpy as np

# Simple in-memory vector store
vector_db = []

def store_vector(text, embedding):
    vector_db.append({
        "text": text,
        "embedding": embedding
    })

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search(query_embedding, top_k=3):
    similarities = []

    for item in vector_db:
        sim = cosine_similarity(query_embedding, item["embedding"])
        similarities.append((sim, item["text"]))

    similarities.sort(reverse=True)

    results = [text for _, text in similarities[:top_k]]
    return results