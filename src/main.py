import openai
import faiss
import numpy as np

class PromptOptimizer:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.vector_store = faiss.IndexFlatL2(768)  # Assuming embedding size of 768

    def embed_text(self, text):
        response = openai.Embedding.create(
            input=[text],
            model="text-embedding-ada-002"  # Change model if needed
        )
        return np.array(response['data'][0]['embedding']).astype('float32')

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