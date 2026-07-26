class ResumeScorer:

    @staticmethod
    def calculate_skill_score(candidate_skills,
                              required_skills):

        if not required_skills:
            return 0

        matched = len(

            set(candidate_skills)

            &

            set(required_skills)

        )

        return (

            matched

            /

            len(required_skills)

        ) * 100

    @staticmethod
    def calculate_experience_score(years):

        if years >= 5:
            return 100

        if years >= 3:
            return 80

        if years >= 1:
            return 60

        return 40

    @staticmethod
    def calculate_education_score(education):

        text = " ".join(education).lower()

        if "computer science" in text:
            return 100

        if "engineering" in text:
            return 80

        return 50

    @staticmethod
    def calculate_project_score(projects):

        if len(projects) >= 3:
            return 100

        if len(projects) >= 1:
            return 70

        return 40

    @staticmethod
    def calculate_final_score(
            info,
            similarity,
            required_skills
    ):

        skill = ResumeScorer.calculate_skill_score(

            info["skills"],

            required_skills

        )

        experience = ResumeScorer.calculate_experience_score(

            info["experience_years"]

        )

        education = ResumeScorer.calculate_education_score(

            info["education"]

        )

        projects = ResumeScorer.calculate_project_score(

            info["projects"]

        )

        semantic = similarity * 100

        final = (

                skill * 0.45 +

                semantic * 0.25 +

                experience * 0.15 +

                education * 0.10 +

                projects * 0.05

        )

        return {

            "skill_score": round(skill, 2),

            "semantic_score": round(semantic, 2),

            "experience_score": round(experience, 2),

            "education_score": round(education, 2),

            "project_score": round(projects, 2),

            "final_score": round(final, 2)
        }