import re


class JDAnalyzer:

    COMMON_SKILLS = [

        "Python",
        "Java",
        "C",
        "C++",
        "SQL",
        "MySQL",
        "PostgreSQL",
        "MongoDB",

        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Angular",

        "Flask",
        "FastAPI",
        "Django",

        "Docker",
        "Kubernetes",

        "AWS",
        "Azure",
        "GCP",

        "Git",
        "GitHub",

        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "OpenCV",

        "Pandas",
        "NumPy",

        "Apache NiFi",
        "ETL",

        "Power BI",
        "Tableau",
        "Metabase",

        "LLM",
        "RAG",

        "Prompt Engineering",

        "REST API"

    ]

    @staticmethod
    def extract_required_skills(jd_text):

        found = []

        jd_lower = jd_text.lower()

        for skill in JDAnalyzer.COMMON_SKILLS:

            if skill.lower() in jd_lower:
                found.append(skill)

        return sorted(list(set(found)))