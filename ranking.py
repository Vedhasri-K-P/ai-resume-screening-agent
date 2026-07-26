from typing import List, Dict


class RankingEngine:

    @staticmethod
    def get_decision(score: float) -> str:

        if score >= 70:
            return "Shortlist"

        elif score >= 50:
            return "Review"

        return "Reject"

    @staticmethod
    def rank_candidates(candidates: List[Dict]) -> List[Dict]:

        ranked = sorted(
            candidates,
            key=lambda x: x["final_score"],
            reverse=True
        )

        for index, candidate in enumerate(ranked, start=1):

            candidate["rank"] = index

            candidate["decision"] = RankingEngine.get_decision(
                candidate["final_score"]
            )

        return ranked