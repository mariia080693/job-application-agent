from google.adk.tools import FunctionTool
import pdfplumber

def read_cv(file_path: str) -> str:
    """Reads the contents of a CV.pdf file using pdfplumber for better structure preservation.

    Args:
        file_path: The path to the CV.pdf file.

    Returns:
        The contents of the CV.pdf file as a string.
    """
    if not file_path.lower().endswith('.pdf'):
        raise ValueError("Only PDF files are supported for CV reading.")
    try:
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text.strip()
    except FileNotFoundError:
        return f"Error: The file at {file_path} was not found."
    except Exception as e:
        return f"An unexpected error occurred while reading the PDF: {e}"

read_cv_tool = FunctionTool(
    func=read_cv,
)

