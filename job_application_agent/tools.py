from google.adk.tools import FunctionTool
import pdfplumber
from fpdf import FPDF


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
def save_cover_letter_to_file(cover_letter: str, filename: str = "cover_letter.pdf") -> dict:
    """Saves the cover letter to a PDF file.
    
    Args:
        cover_letter: The cover letter content to save.
        filename: The filename to save to (default cover_letter.pdf).
        
    Returns:
        A dictionary with status and message.
    """
    try:
        if not cover_letter or not cover_letter.strip():
            return {
                "status": "error",
                "message": "Cover letter content is empty or invalid."
            }

        # Initialize PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)

        # Split cover letter into lines for PDF
        lines = cover_letter.strip().split("\n")
        for line in lines:
            pdf.multi_cell(0, 10, line)
        
        # Save PDF
        pdf.output(filename)
        
        return {
            "status": "success",
            "message": f"Cover letter successfully saved to {filename}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to save cover letter: {str(e)}"
        }