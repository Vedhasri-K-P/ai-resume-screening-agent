import os
from groq import Groq


class AIRecommender:

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            self.client = None
            return

        self.client = Groq(api_key=api_key)

    def generate_recommendation(
        self,
        candidate,
        required_skills,
        jd_text,
    ):

        if self.client is None:
            return (
                "AI Recommendation unavailable.\n"
                "Reason: GROQ_API_KEY not configured."
            )

        prompt = f"""
You are an experienced HR recruiter.

Evaluate the candidate against the job description.

Job Description

{jd_text}

Required Skills

{", ".join(required_skills)}

Candidate Name:
{candidate["name"]}

Skills:
{", ".join(candidate["skills"])}

Education:
{", ".join(candidate["education"])}

Experience:
{candidate["experience_years"]} years

Similarity:
{candidate["similarity"]}%

Final Score:
{candidate["final_score"]}

Respond in this format only:

Overall Assessment:
...

Strengths:
- ...
- ...

Weaknesses:
- ...
- ...

Recommendation:
...
"""

        try:

            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                temperature=0.2,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a senior HR recruiter."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response.choices[0].message.content

        except Exception as e:

            return (
                "AI Recommendation unavailable.\n"
                f"Reason: {str(e)}"
            )
            