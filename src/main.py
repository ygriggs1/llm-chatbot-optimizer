import openai
import faiss
import numpy as np

# text-embedding-ada-002 produces 1536-dimensional embeddings
EMBEDDING_DIM = 1536
EMBEDDING_MODEL = "text-embedding-ada-002"


class PromptOptimizer:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)
        self.vector_store = faiss.IndexFlatL2(EMBEDDING_DIM)

    def embed_text(self, text):
        response = self.client.embeddings.create(
            input=[text],
            model=EMBEDDING_MODEL,
        )
        return np.array(response.data[0].embedding).astype("float32")

    def add_to_vector_store(self, text):
        embedding = self.embed_text(text)
        self.vector_store.add(embedding.reshape(1, -1))

    def query_vector_store(self, query, k=5):
        query_embedding = self.embed_text(query)
        distances, indices = self.vector_store.search(query_embedding.reshape(1, -1), k)
        return indices, distances


# Example usage:
# optimizer = PromptOptimizer(api_key='your_openai_api_key')
# optimizer.add_to_vector_store("What is the capital of France?")
# indices, distances = optimizer.query_vector_store("What is the capital of France?")
# print(indices, distances)