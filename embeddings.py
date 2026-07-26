from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL


class EmbeddingEngine:

    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer(EMBEDDING_MODEL)

        print("Embedding model loaded successfully.")

    def generate_embedding(self, text):

        return self.model.encode(
            text,
            convert_to_tensor=True,
            normalize_embeddings=True
        )