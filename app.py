from pathlib import Path

from rich.console import Console
from rich.panel import Panel

from src.parser import ResumeParser
from src.extractor import ResumeExtractor
from src.embeddings import EmbeddingEngine
from src.similarity import SimilarityEngine
from src.scoring import ResumeScorer
from src.jd_analyzer import JDAnalyzer
from src.ranking import RankingEngine
from src.exporter import Exporter

from src.recommender import AIRecommender

console = Console()


def banner():
    console.print(
        Panel.fit(
            "[bold cyan]AI Resume Screening Agent[/bold cyan]\n"
            "[white]Debug Mode - Resume Extraction[/white]",
            border_style="green",
        )
    )


def main():

    banner()

    # ------------------------------------
    # Load Embedding Model
    # ------------------------------------

    embedding_engine = EmbeddingEngine()

    # ------------------------------------
    # AI Recommender
    # ------------------------------------

    recommender = AIRecommender()


    # ------------------------------------
    # Load Job Description
    # ------------------------------------

    jd_path = Path("data/job_description/software_engineer_jd.txt")

    jd_text = jd_path.read_text(encoding="utf-8")

    required_skills = JDAnalyzer.extract_required_skills(jd_text)

    console.print("\n[bold cyan]Required Skills[/bold cyan]")
    console.print(required_skills)

    jd_embedding = embedding_engine.generate_embedding(jd_text)

    # ------------------------------------
    # Resume Folder
    # ------------------------------------

    resume_folder = Path("data/resumes")

    resumes = list(resume_folder.iterdir())

    if not resumes:
        console.print("[red]No resumes found![/red]")
        return

    # ------------------------------------
    # Debug Folder
    # ------------------------------------

    debug_folder = Path("output/debug")
    debug_folder.mkdir(parents=True, exist_ok=True)

    # ------------------------------------
    # Candidate Results
    # ------------------------------------

    candidates = []

    # ------------------------------------
    # Process Every Resume
    # ------------------------------------

    for resume in resumes:

        console.rule(f"[yellow]{resume.name}")

        # Extract Resume Text

        resume_text = ResumeParser.extract_text(resume)

        # Save Raw Resume Text

        debug_file = debug_folder / f"{resume.stem}.txt"

        with open(debug_file, "w", encoding="utf-8") as f:
            f.write(resume_text)

        console.print(
            f"[green]Raw extracted text saved to:[/green] {debug_file}"
        )

        # Preview Resume

        console.print("\n[bold cyan]RAW RESUME TEXT[/bold cyan]\n")
        console.print(resume_text[:1500])

        console.print("\n" + "=" * 80)

        # ------------------------------------
        # Extract Resume Information
        # ------------------------------------

        info = ResumeExtractor.extract_resume_information(resume_text)

        console.print(f"[bold green]Extracted Name:[/bold green] {info['name']}")
        console.print("\n[bold green]EXTRACTED INFORMATION[/bold green]\n")
        console.print(info)

        # ------------------------------------
        # Generate Embeddings
        # ------------------------------------

        resume_embedding = embedding_engine.generate_embedding(
            resume_text
        )

        similarity = SimilarityEngine.calculate_similarity(
            resume_embedding,
            jd_embedding
        )

        # ------------------------------------
        # Calculate Resume Score
        # ------------------------------------

        scores = ResumeScorer.calculate_final_score(
            info,
            similarity,
            required_skills,
        )

        console.print("\n[bold cyan]SCORE BREAKDOWN[/bold cyan]\n")
        console.print(scores)

        console.print(
            f"\n[bold yellow]Semantic Similarity : {similarity:.3f}[/bold yellow]"
        )

        # ------------------------------------
        # Store Candidate
        # ------------------------------------

        candidate = {
    "name": (
        info["name"]
        if info["name"] != "Unknown"
        else resume.stem
    ),
    "file_name": resume.name,

    "skills": info["skills"],
    "education": info["education"],
    "experience_years": info["experience_years"],

    "similarity": round(similarity * 100, 2),

    "skill_score": scores["skill_score"],
    "experience_score": scores["experience_score"],
    "education_score": scores["education_score"],
    "project_score": scores["project_score"],

    "final_score": scores["final_score"],
}

        candidates.append(candidate)

        console.print("\n" + "-" * 100 + "\n")

    # ====================================
    # Rank Candidates
    # ====================================

        ranked_candidates = RankingEngine.rank_candidates(candidates)

    # ====================================
    # AI Recommendations
    # ====================================

    console.rule("[bold magenta]AI RECOMMENDATIONS[/bold magenta]")

    for candidate in ranked_candidates:

        recommendation = recommender.generate_recommendation(
            candidate,
            required_skills,
            jd_text,
        )

    candidate["recommendation"] = recommendation

    console.print(f"\n[bold]{candidate['name']}[/bold]")
    console.print(recommendation)

    # ====================================
    # Export Results
    # ====================================

    csv_file = Exporter.export_csv(ranked_candidates)

    json_file = Exporter.export_json(ranked_candidates)

    # ====================================
    # Display Final Ranking
    # ====================================

    console.rule("[bold green]FINAL RANKING[/bold green]")

    for candidate in ranked_candidates:

        console.print(
            f"""
                [bold]Rank[/bold]        : {candidate['rank']}
                [bold]Candidate[/bold]   : {candidate['name']}
                [bold]File[/bold]        : {candidate['file_name']}
                [bold]Score[/bold]       : {candidate['final_score']}
                [bold]Decision[/bold]    : {candidate['decision']}
                [bold]Similarity[/bold]  : {candidate['similarity']}%
            """
            )

    # ====================================
    # Export Summary
    # ====================================

    console.rule("[bold cyan]EXPORT COMPLETE[/bold cyan]")

    console.print(
        f"[green]CSV exported:[/green] {csv_file}"
    )

    console.print(
        f"[green]JSON exported:[/green] {json_file}"
    )


if __name__ == "__main__":
    main()