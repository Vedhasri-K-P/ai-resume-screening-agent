from src.recommender import AIRecommender

candidate = {
    "name": "John Doe",
    "skills": ["Python", "SQL"],
    "education": ["B.E Computer Science"],
    "experience_years": 2,
    "similarity": 82.5,
    "final_score": 84.2,
}

required_skills = [
    "Python",
    "SQL",
    "Docker"
]

jd_text = """
Looking for a Python Developer with SQL and Docker experience.
"""

recommender = AIRecommender()

print(
    recommender.generate_recommendation(
        candidate,
        required_skills,
        jd_text
    )
)