from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from .config import config
from .sub_agents import (
    robust_data_scientist_searcher,
    cover_letter_planner,
 #   cover_letter_writer,
 #   cover_letter_editor,
)

from .tools import read_cv

# --- AGENT DEFINITIONS ---

interactive_job_application_agent = Agent(
    name="interactive_job_application_agent",
    model=config.worker_model,
    description="A job application assistant that helps users search for Data Scientist jobs and create cover letters.",
    instruction="""You are Your Friendly HR Charlie, a job application assistant specializing in Data Scientist roles in Melbourne.

IMPORTANT: When the user first contacts you, introduce yourself by saying 'Hi, I am Your Friendly HR Charlie. I am happy to assist you with your job search and application process!' and then:

1. Use robust_data_scientist_searcher to find the **single most recent** Data Scientist job posting in Melbourne, Australia (posted within the last 3 days if possible).
2. You must complete the preceding step and directly moving to the next one without waighting for the user feedback
   Use read_cv to load and extract text from the file 'CV.pdf' with job applicant information in the project directory. Never ask the user for a path; always read from 'CV.pdf'.
   After extraction, transform content of the 'CV.pdf' file into a clean, well-structured document. Organize it into clear sections (e.g., Education, Experience, Skills, Publications) and format it for easy reading.
   Present the information clearly and neatly so the user can quickly understand information from the 'CV.pdf'.
3. You must complete the preceding step step before moving to this one. Use cover_letter_planner to create a good structure for a cover letter based on the job description and the data extracted from the user's CV.
""",
    sub_agents=[robust_data_scientist_searcher, cover_letter_planner],
    tools=[FunctionTool(read_cv)],
    output_key="final_cover_letter",
)

root_agent = interactive_job_application_agent
