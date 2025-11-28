from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from job_application_agent.tools import read_cv
from ..config import config
import datetime

CV_READER_INSTRUCTION = """
You are a professional CV reader.
Use read_cv tool to load and extract text from the file 'CV.pdf' with job applicant information in the project directory. Never ask the user for a path; always read from 'CV.pdf'.
After extraction, transform content of the 'CV.pdf' file into a clean, well-structured document. Organize it into clear sections (e.g., Education, Experience, Skills, Publications) and format it for easy reading.
You must display the information clearly and neatly so the user can quickly understand information from the 'CV.pdf'.
"""

cv_reader = Agent(
    name="cv_reader",
    model=config.worker_model,
    instruction=CV_READER_INSTRUCTION,
    tools=[FunctionTool(read_cv)],
    output_key="cv_content",
)