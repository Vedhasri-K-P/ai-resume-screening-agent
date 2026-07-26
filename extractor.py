import re
from typing import Dict, List


class ResumeExtractor:

    # ==========================================
    # COMMON TECHNICAL SKILLS
    # ==========================================

    SKILLS = sorted(set([

        "Python",
        "Java",
        "C",
        "C++",
        "SQL",
        "MySQL",
        "PostgreSQL",
        "MongoDB",
        "Oracle",

        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Angular",
        "Node.js",

        "Flask",
        "FastAPI",
        "Django",

        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "OpenCV",
        "Scikit-learn",

        "Pandas",
        "NumPy",

        "Apache NiFi",
        "ETL",
        "Data Pipeline",

        "Docker",
        "Kubernetes",

        "AWS",
        "Azure",
        "GCP",

        "Git",
        "GitHub",

        "Power BI",
        "Tableau",
        "Metabase",

        "LLM",
        "RAG",
        "Prompt Engineering",

        "REST API"

    ]))

    # ==========================================

    @staticmethod
    def normalize(text):

        text = text.replace("\t", " ")

        cleaned_lines = []

        for line in text.splitlines():

            line = re.sub(r"\s+", " ", line).strip()

            if line:
                cleaned_lines.append(line)

        return "\n".join(cleaned_lines)

    # ==========================================

    @staticmethod
    def extract_email(text):

        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        match = re.search(pattern, text)

        return match.group(0) if match else ""

    # ==========================================

    @staticmethod
    def extract_phone(text):

        pattern = r"(\+91[\s-]?)?[6-9]\d{9}"

        match = re.search(pattern, text)

        return match.group(0) if match else ""

    # ==========================================

    @staticmethod
    def extract_name(text):

        skip_words = [
            "resume",
            "curriculum",
            "vitae",
            "email",
            "phone",
            "linkedin",
            "github",
            "summary",
            "professional summary",
            "technical skills",
            "skills",
            "education",
            "experience",
            "projects",
            "certifications",
            "internship",
            "india",
            "@",
            "+91"
        ]

        for line in text.splitlines()[:10]:

            line = line.strip()

            if not line:
                continue

            if len(line) > 40:
                continue

            if any(ch.isdigit() for ch in line):
                continue

            if any(word in line.lower() for word in skip_words):
                continue

            words = line.split()

            if 2 <= len(words) <= 4:
                return line.title()

        return "Unknown"

    # ==========================================

    @staticmethod
    def extract_github(text):

        match = re.search(
            r"https?://github\.com/[^\s]+",
            text,
            re.IGNORECASE
        )

        return match.group(0) if match else ""

    # ==========================================

    @staticmethod
    def extract_linkedin(text):

        match = re.search(
            r"https?://(www\.)?linkedin\.com/[^\s]+",
            text,
            re.IGNORECASE
        )

        return match.group(0) if match else ""

    # ==========================================

    @staticmethod
    def extract_skills(text):

        skills = []

        lower = text.lower()

        for skill in ResumeExtractor.SKILLS:

            if skill.lower() in lower:

                skills.append(skill)

        return sorted(set(skills))

    # ==========================================

    @staticmethod
    def extract_experience(text):

        years = 0

        matches = re.findall(
            r"(\d+)\+?\s*(year|years)",
            text.lower()
        )

        if matches:

            years = max(int(i[0]) for i in matches)

        return years

    # ==========================================

    @staticmethod
    def extract_sections(text) -> Dict:

        headings = [

            "education",

            "experience",

            "projects",

            "technical skills",

            "skills",

            "certifications",

            "internship",

            "internships"

        ]

        sections = {}

        current = "general"

        sections[current] = ""

        for line in text.split("\n"):

            line_clean = line.strip().lower()

            matched = False

            for heading in headings:

                if heading == line_clean:

                    current = heading

                    sections[current] = ""

                    matched = True

                    break

            if not matched:

                sections[current] += line + "\n"

        return sections

    # ==========================================

    @staticmethod
    def extract_projects(section_text):

        projects = []

        for line in section_text.split("\n"):

            line = line.strip()

            if len(line) > 10:

                projects.append(line)

        return projects

    # ==========================================

    @staticmethod
    def extract_education(section):

        education = []

        keywords = [

            "Bachelor",

            "B.E",

            "B.Tech",

            "Master",

            "M.Tech",

            "Computer Science",

            "Engineering"

        ]

        for keyword in keywords:

            if keyword.lower() in section.lower():

                education.append(keyword)

        return sorted(set(education))

    # ==========================================

    @staticmethod
    def extract_certifications(section):

        certs = []

        for line in section.split("\n"):

            if len(line.strip()) > 5:

                certs.append(line.strip())

        return certs

    # ==========================================

    @staticmethod
    def extract_resume_information(text):

        text = ResumeExtractor.normalize(text)

        sections = ResumeExtractor.extract_sections(text)

        return {

            "name": ResumeExtractor.extract_name(text),

            "email": ResumeExtractor.extract_email(text),

            "phone": ResumeExtractor.extract_phone(text),

            "github": ResumeExtractor.extract_github(text),

            "linkedin": ResumeExtractor.extract_linkedin(text),

            "skills": ResumeExtractor.extract_skills(text),

            "education": ResumeExtractor.extract_education(

                sections.get("education", text)

            ),

            "experience_years": ResumeExtractor.extract_experience(text),

            "projects": ResumeExtractor.extract_projects(

                sections.get("projects", "")

            ),

            "certifications": ResumeExtractor.extract_certifications(

                sections.get("certifications", "")

            )
        }