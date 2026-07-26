# AI Resume Screening Agent

## Project Overview

This project is an AI-powered Resume Screening Agent developed as part of the **ROOMAN Technologies – 24 Hour AI Agent Challenge**.

The purpose of this project is to help recruiters quickly compare multiple resumes against a given Job Description (JD) and rank candidates based on how well they match the required skills and qualifications.

Instead of manually reading every resume, the application automatically extracts important information, compares it with the job description, calculates a relevance score, and generates a ranked list of candidates.

---

# Features

- Reads resumes in PDF format
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

```
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
```

---

# Technologies Used

- Python
- Sentence Transformers
- Hugging Face
- Scikit-Learn
- PyPDF
- Rich (Console Output)
- Groq (Optional AI Recommendation)

---

# Installation

Clone the repository.

```bash
git clone <repository-url>
```

Go inside the project.

```bash
cd AI-Resume-Screening-Agent
```

Install the required packages.

```bash
pip install -r requirements.txt
```

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

# Output

The application generates two output files.

### rankings.csv

Contains the ranked list of all candidates.

Example:

| Rank | Candidate | Score | Decision |
|------|-----------|--------|-----------|
|1|John Doe|87.25|Shortlist|

---

### rankings.json

Contains the complete candidate information in JSON format.

---

# Scoring Method

The final score is calculated using multiple factors.

- Skill Match
- Semantic Similarity
- Experience
- Education
- Projects

Each factor contributes a weighted score.

The combined score determines the final ranking.

This makes the evaluation more balanced instead of relying only on keyword matching.

---

# Similarity Calculation

This project uses the Sentence Transformer model to convert both the resume and the Job Description into vector embeddings.

Cosine Similarity is then used to calculate how closely the resume matches the Job Description.

This allows the application to understand the overall meaning of the resume instead of matching only exact words.

---

# Assumptions

- Resumes are provided in PDF format.
- A Job Description is available before screening begins.
- Candidates are ranked only against the provided Job Description.
- The application processes all resumes present in the resume folder.

---

# Current Limitations

This project works well for the challenge but still has a few limitations.

- Resume parsing depends on the quality of the PDF.
- Experience calculation can be improved.
- Name extraction may fail for some resume formats.
- Only PDF resumes are currently supported.
- The scoring weights are fixed.

These can be improved in future versions.

---

# Future Improvements

Some possible improvements are:

- Support DOCX resumes
- Better resume parsing
- OCR support for scanned resumes
- Custom scoring weights
- Web interface
- Recruiter dashboard
- Better experience extraction
- Candidate recommendation using Large Language Models

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
