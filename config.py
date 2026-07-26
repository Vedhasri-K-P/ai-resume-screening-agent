from dotenv import load_dotenv
import os

load_dotenv()

# ===========================
# API CONFIGURATION
# ===========================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ===========================
# AI MODELS
# ===========================

LLM_MODEL = "llama-3.3-70b-versatile"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ===========================
# PROJECT PATHS
# ===========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(BASE_DIR, "data")
RESUME_FOLDER = os.path.join(DATA_FOLDER, "resumes")
JD_FOLDER = os.path.join(DATA_FOLDER, "job_description")

OUTPUT_FOLDER = os.path.join(BASE_DIR, "output")
REPORT_FOLDER = os.path.join(OUTPUT_FOLDER, "reports")

# ===========================
# SCORING WEIGHTS
# ===========================

WEIGHTS = {
    "skills": 0.45,
    "semantic_similarity": 0.25,
    "experience": 0.15,
    "education": 0.10,
    "projects": 0.05
}