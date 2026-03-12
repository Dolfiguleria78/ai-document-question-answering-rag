from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    """
    Convert text into vector embedding
    """
    embedding = model.encode(text)
    return embedding