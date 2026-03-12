# AI Document Question Answering (RAG)

## Overview
This project implements a Retrieval-Augmented Generation (RAG) system that allows users to ask questions based on document content.

## Features
- Document loading
- Text embeddings
- Vector similarity search
- Retrieval-based question answering

## Tech Stack
- Python
- Sentence Transformers
- Vector embeddings

## Project Structure
app.py – main application
embedder.py – converts text to embeddings
vector_store.py – stores document vectors
rag_pipeline.py – retrieval pipeline
document_loader.py – loads documents

## How to Run
1. Clone the repository
2. Install dependencies
3. Run:

python app.py