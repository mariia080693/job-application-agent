from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from ..config import config
from ..tools import read_cv

CV_CONVERTER_INSTRUCTION = """
You are a CV converter.
Your goal is to read a user's CV from a PDF file and convert it into a clean, readable Markdown format.

The CV file is located at "CV.pdf" in the project directory.
Use the read_cv tool with the file path "CV.pdf" to extract the text from the PDF.
DO NOT ask the user for the file path - always use "CV.pdf".

After extracting the CV text, convert it to clean Markdown format with proper sections and formatting.
Output your result as 'cv_markdown'.
"""

cv_converter = Agent(
    name="cv_converter",
    model=config.worker_model,
    instruction=CV_CONVERTER_INSTRUCTION,
    tools=[FunctionTool(read_cv)],
    output_key="cv_markdown",
)
