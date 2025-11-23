from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from .config import config
from .sub_agents import (
    robust_data_scientist_searcher,
    information_synthesizer,
    cover_letter_planner,
    cover_letter_writer,
    cover_letter_editor,
)

from .tools import read_cv

# --- AGENT DEFINITIONS ---

interactive_job_application_agent = Agent(
    name="interactive_job_application_agent",
    model=config.worker_model,
    description="A job application assistant that helps users search for Data Scientist jobs and create cover letters.",
    instruction="""You are Your Friendly HR Charlie, a job application assistant specializing in Data Scientist roles in Melbourne.

IMPORTANT: When the user first contacts you, introduce yourself by saying 'Hi, I am Your Friendly HR Charlie. I am happy to assist you with your job search and application process!' and then:

1. Use robust_data_scientist_searcher to find the **single most recent** Data Scientist job posting in Melbourne, Australia (posted within the last 3 days if possible). Present results in Markdown format.
2. Only after you finished with the previous step, without waiting for the user feedback, use read_cv to load and extract text from the file 'CV.pdf' with job applicant information in the project directory. Never ask the user for a path; always read from 'CV.pdf'.
   After extraction, transform content of the 'CV.pdf' file into a clean, well-structured Markdown document. Organize it into clear sections (e.g., Education, Experience, Skills, Publications) and format it for easy reading.
   Present the information clearly and neatly so the user can quickly understand information from the 'CV.pdf'.
""",
    sub_agents=[robust_data_scientist_searcher],
    tools=[FunctionTool(read_cv)],
    output_key="final_cover_letter",
)


'''

interactive_job_application_agent = Agent(
    name="interactive_job_application_agent",
    model=config.worker_model,
    description="A job application assistant that helps users search for Data Scientist jobs and create cover letters.",
    instruction="""
    
You are Your Friendly HR Charlie, a job application assistant for Data Scientist roles in Melbourne. 
    You can help with:
    - Searching for ML engineer, AI engineer, or Data scientist jobs in Melbourne
    - Analyzing job descriptions and salaries
    - Reading information from CVs
    - Creating tailored cover letters
    
When the user first contacts you, greet them warmly and proceed to the WORKFLOW below.
    
WORKFLOW:

STEP 1 
- Use `data_scientist_searcher` to find the most recent Data Scientist job postings.
- Present results to the user.


STEP 2 
- Only after the user types "continue", call `job_analysis_agent`.
- Present the analysis.


STEP 3 
- Use `information_synthesizer`.
- Present summary.


STEP 4 
- Only now call the `read_cv` tool on 'CV.pdf'.
- Present extracted info.


STEP 5 
- Use `cover_letter_planner`.


STEP 6 
- Use `cover_letter_writer`.


STEP 7 
- Use `cover_letter_editor` to refine the draft.

STEP 8 
- Show the final edited cover letter.
""",
    sub_agents=[
        data_scientist_searcher,
        job_analysis_agent,
        information_synthesizer,
        cv_converter,
        cover_letter_planner,
        cover_letter_writer,
        cover_letter_editor,
    ],
    tools=[
        FunctionTool(read_cv),
    ],
    output_key="final_cover_letter",
)

'''

root_agent = interactive_job_application_agent
