import csv
import json
from pathlib import Path


class Exporter:

    OUTPUT_DIR = Path("output")

    @staticmethod
    def export_csv(candidates):

        Exporter.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        csv_path = Exporter.OUTPUT_DIR / "rankings.csv"

        with open(csv_path, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Rank",
                "Candidate",
                "File",
                "Final Score",
                "Similarity",
                "Decision"
            ])

            for candidate in candidates:

                writer.writerow([
                    candidate["rank"],
                    candidate["name"],
                    candidate["file_name"],
                    candidate["final_score"],
                    candidate["similarity"],
                    candidate["decision"]
                ])

        return csv_path

    @staticmethod
    def export_json(candidates):

        Exporter.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        json_path = Exporter.OUTPUT_DIR / "rankings.json"

        with open(json_path, "w", encoding="utf-8") as file:

            json.dump(
                candidates,
                file,
                indent=4
            )

        return json_path