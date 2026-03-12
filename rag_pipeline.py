from embedder import get_embedding
from vector_store import store_vector, search


def add_document(text):
    embedding = get_embedding(text)
    store_vector(text, embedding)


def ask_question(question):
    query_embedding = get_embedding(question)
    results = search(query_embedding)

    if results:
        return results[0]   # return the most relevant document
    else:
        return "No relevant information found."