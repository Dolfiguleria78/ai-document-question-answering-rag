from rag_pipeline import add_document, ask_question
from document_loader import load_documents

# Load documents
documents = load_documents("data/documents")

# Add documents to vector store
for doc in documents:
    add_document(doc)

print("RAG System Ready!")
print("Ask a question (type 'exit' to quit)\n")

while True:
    question = input("Your question: ")

    if question.lower() == "exit":
        break

    answer = ask_question(question)
    print("\nAnswer:", answer, "\n")