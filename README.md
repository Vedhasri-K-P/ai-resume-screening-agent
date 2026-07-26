# AI Resume Screening Agent

## Project Overview

This project is an AI-powered Resume Screening Agent developed as part of the **ROOMAN Technologies – 24 Hour AI Agent Challenge**.

The purpose of this project is to help recruiters quickly compare multiple resumes against a given Job Description (JD) and rank candidates based on how well they match the required skills and qualifications.

Instead of manually reading every resume, the application automatically extracts important information, compares it against the job description, calculates a weighted relevance score, and generates a ranked list of candidates.

---

# Features

- Supports parsing resumes in PDF, DOCX and TXT formats.
- Extracts important candidate information
  - Skills
  - Education
  - Experience
- Reads a Job Description
- Identifies the required skills from the Job Description
- Generates semantic embeddings using Sentence Transformers
- Calculates similarity using Cosine Similarity
- Uses a weighted scoring system to score each candidate
- Ranks all candidates from highest to lowest score
- Exports the results to CSV and JSON format
- Supports screening multiple resumes in a single run

---

# Project Structure

```
AI-Resume-Screening-Agent/

│
├── app.py
│
├── data/
│   ├── resumes/
│   └── job_description/
│
├── src/
│   ├── parser.py
│   ├── extractor.py
│   ├── embeddings.py
│   ├── similarity.py
│   ├── scoring.py
│   ├── jd_analyzer.py
│   ├── ranking.py
│   ├── exporter.py
│   └── recommender.py
│
├── output/
│   ├── debug/
│   ├── rankings.csv
│   └── rankings.json
│
├── requirements.txt
│
└── README.md
```

---

# How It Works

The complete workflow of the application is shown below.

Job Description
        │
        ▼
Extract Required Skills
        │
        ▼
Read Resume
        │
        ▼
Extract Candidate Information
        │
        ▼
Generate Embeddings
        │
        ▼
Calculate Semantic Similarity
        │
        ▼
Calculate Final Score
        │
        ▼
Rank Candidates
        │
        ▼
Export Results (CSV & JSON)

---

# System Architecture

The application follows a modular pipeline where each component is responsible for a specific task.

```text
                 ┌───────────────────────────┐
                 │   Job Description (JD)    │
                 └─────────────┬─────────────┘
                               │
                               ▼
                    JD Analyzer (Skills)
                               │
                               ▼
                 ┌───────────────────────────┐
                 │       Resume Parser       │
                 │ (PDF / DOCX / TXT Reader) │
                 └─────────────┬─────────────┘
                               │
                               ▼
                  Resume Information Extractor
       (Name, Skills, Education, Experience, Projects)
                               │
                               ▼
                    Embedding Generation
          (SentenceTransformer - all-MiniLM-L6-v2)
                               │
                               ▼
                   Semantic Similarity Engine
                         (Cosine Similarity)
                               │
                               ▼
                    Weighted Scoring Engine
                               │
                               ▼
                      Candidate Ranking
                               │
                               ▼
          AI Recommendation Engine (Optional - Groq)
                               │
                               ▼
                 CSV & JSON Result Export
```

---

# Technologies Used

- Python
- Sentence Transformers
- Hugging Face Transformers
- Scikit-Learn
- PyPDF2
- Rich (Console Output)
- Groq (Optional AI Recommendation)

---

# Installation

Clone the repository.

```bash
git clone https://github.com/<your-username>/AI-Resume-Screening-Agent.git
```

Go inside the project.

```bash
cd AI-Resume-Screening-Agent
```

Install the required packages.

```bash
pip install -r requirements.txt
```

## Optional Configuration

The AI recommendation feature uses the Groq API.

Create an environment variable named:

```
GROQ_API_KEY
```

and assign your Groq API key.

If the API key is not configured, the resume screening pipeline will continue to work normally, but AI-generated recommendations will be unavailable.

---

# Project Setup

Place all resumes inside:

```
data/resumes/
```

Place the Job Description inside:

```
data/job_description/
```

The current project expects the Job Description file as:

```
software_engineer_jd.txt
```

---

# Running the Project

Run the application using:

```bash
python app.py
```

The application will:

- Read all resumes
- Extract candidate details
- Compare them with the Job Description
- Calculate similarity
- Rank candidates
- Export the final results

---

### Sample Data

The repository includes sample resumes, a sample job description, and sample output files to help reviewers quickly understand and test the application. You can replace the sample resumes and job description with your own files to evaluate different candidates and roles.

---

# Output

The application generates two output files.

### rankings.csv

The CSV file contains the ranked list of candidates.

| Rank | Candidate | File | Final Score | Similarity | Decision |
|------|-----------|------|------------:|-----------:|----------|
|1|Ananya Rao|resume1.pdf|70.02|72.06|Shortlist|
|2|Nikhil Reddy|resume4.pdf|61.25|70.98|Review|
|3|Arjun Patel|resume6.pdf|56.10|60.39|Review|

#### Column Description

- **Rank** – Candidate position after ranking
- **Candidate** – Extracted candidate name
- **File** – Resume filename
- **Final Score** – Overall weighted score
- **Similarity** – Semantic similarity percentage
- **Decision** – Shortlist, Review or Reject

---

### rankings.json

The JSON file stores complete candidate information in a structured format, including:

- Candidate Name
- Resume Filename
- Extracted Skills
- Education
- Experience
- Semantic Similarity
- Individual Score Components
- Final Score
- Rank
- Decision
- AI Recommendation (if enabled)
---

# Scoring Method

The final score is calculated using the following weighted criteria:

| Criteria | Weight |
|----------|-------:|
| Skill Match | 45% |
| Semantic Similarity | 25% |
| Experience | 15% |
| Education | 10% |
| Projects | 5% |

These weighted scores are combined to calculate the final candidate score.

Candidates are then ranked from highest to lowest score.
---

# Similarity Calculation

The project uses the `sentence-transformers/all-MiniLM-L6-v2` embedding model to convert resumes and the Job Description into vector representations.

Cosine Similarity is then used to measure how closely each resume matches the Job Description based on semantic meaning rather than exact keyword matching.
---

# Candidate Decision

Based on the final score, candidates are classified into one of the following categories:

| Final Score | Decision |
|-------------|----------|
| 70 and above | Shortlist |
| 50 – 69.99 | Review |
| Below 50 | Reject |

This allows recruiters to quickly identify strong candidates while keeping promising applicants under review.

---

# Assumptions

- Resumes can be provided in PDF, DOCX or TXT format.
- A Job Description is available before screening begins.
- Candidates are ranked only against the provided Job Description.
- The application processes all resumes available in the resume folder.

---

# Current Limitations

This project works well for the challenge but still has a few limitations.

- Resume parsing depends on the quality and layout of the source document.
- Name extraction may require additional tuning for highly customised resume templates.
- Experience calculation is based on pattern matching and may not capture all formats.
- The scoring weights are fixed.
- AI recommendations require a valid Groq API key.

These can be improved in future versions.

---

# Future Improvements

Some possible improvements are:

- OCR support for scanned resumes
- Better resume parsing for different resume layouts
- Configurable scoring weights
- Web-based user interface
- Recruiter dashboard
- Improved experience extraction
- Better name and education extraction
- Support for additional resume formats such as HTML
- AI-generated interview questions for shortlisted candidates

---

# Why I Chose This Approach

The main goal of this project was to build a working end-to-end resume screening system within the 24-hour challenge.

Instead of making the project unnecessarily complex, I focused on building a complete pipeline that is easy to understand, easy to run, and produces meaningful results.

The scoring combines semantic similarity with candidate information so that resumes are evaluated using both context and structured information.

---

# Conclusion

This project demonstrates how AI can simplify the resume screening process by automatically comparing resumes with a Job Description, calculating relevance scores, and ranking candidates.

The application reduces manual effort and provides recruiters with a quick way to identify the most relevant candidates.

Although there is room for future improvement, the current implementation provides a complete end-to-end resume screening workflow suitable for the challenge.

---

# License

This project was developed for the ROOMAN Technologies – 24 Hour AI Agent Challenge.

It is intended for educational and demonstration purposes.
