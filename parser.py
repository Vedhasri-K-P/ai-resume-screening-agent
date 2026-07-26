from pathlib import Path
import PyPDF2
import docx


class ResumeParser:

    @staticmethod
    def clean_text(text: str) -> str:
        """
        Clean extracted text while preserving line breaks.
        """

        if not text:
            return ""

        cleaned_lines = []

        for line in text.splitlines():

            line = line.replace("\t", " ")

            while "  " in line:
                line = line.replace("  ", " ")

            line = line.strip()

            if line:
                cleaned_lines.append(line)

        return "\n".join(cleaned_lines)

    @staticmethod
    def read_pdf(file_path):

        text = ""

        try:

            with open(file_path, "rb") as file:

                reader = PyPDF2.PdfReader(file)

                for page in reader.pages:

                    extracted = page.extract_text()

                    if extracted:
                        text += extracted + "\n"

        except Exception as e:

            raise Exception(f"Unable to read PDF: {e}")

        return ResumeParser.clean_text(text)
    @staticmethod
    def read_docx(file_path):

        try:

            document = docx.Document(file_path)

            paragraphs = []

            for paragraph in document.paragraphs:
                paragraphs.append(paragraph.text)

            return ResumeParser.clean_text("\n".join(paragraphs))

        except Exception as e:

            raise Exception(f"Unable to read DOCX: {e}")

    @staticmethod
    def read_txt(file_path):

        try:

            with open(file_path, "r", encoding="utf-8") as file:

                text = file.read()

            return ResumeParser.clean_text(text)

        except Exception as e:

            raise Exception(f"Unable to read TXT: {e}")

    @staticmethod
    def extract_text(file_path):

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return ResumeParser.read_pdf(file_path)

        elif extension == ".docx":
            return ResumeParser.read_docx(file_path)

        elif extension == ".txt":
            return ResumeParser.read_txt(file_path)

        else:
            raise Exception(f"Unsupported file type: {extension}")