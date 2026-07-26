from sentence_transformers.util import cos_sim


class SimilarityEngine:

    @staticmethod
    def calculate_similarity(resume_embedding, jd_embedding):

        similarity = cos_sim(
            resume_embedding,
            jd_embedding
        )

        return float(similarity)