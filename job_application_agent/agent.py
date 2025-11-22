import datetime

from google.adk.agents import Agent, ParallelAgent
from google.adk.tools import FunctionTool

from .config import config
from .sub_agents import (
    robust_data_scientist_searcher,
    key_requirements_analyzer,
    secondary_requirements_analyzer,
    company_culture_analyzer,
    information_synthesizer,
    cv_converter,
    cover_letter_planner,
    cover_letter_writer,
    cover_letter_editor,
)

from .tools import read_cv

# --- AGENT DEFINITIONS ---

'''
job_analysis_agent = ParallelAgent(
    name="job_analysis_agent",
    sub_agents=[
        key_requirements_analyzer,
        secondary_requirements_analyzer,
        company_culture_analyzer,
    ],
)
'''

interactive_job_application_agent = Agent(
    name="interactive_job_application_agent",
    model=config.worker_model,
    description="A job application assistant that helps users search for Data Scientist jobs and create cover letters.",
    instruction="""You are Your Friendly HR Charlie, a job application assistant specializing in Data Scientist roles in Melbourne.

When the user first contacts you, greet them warmly and then:

1. Use Google Search to find the **single most recent** Data Scientist job posting in Melbourne, Australia (posted within the last 3 days if possible).

2. Retrieve and present **all important information** from the job posting. 
   Your goal is to extract *comprehensive, structured* details — not just surface-level text.

3. In your output, clearly present the information with the following sections:

   **A. Job Overview**
   - Job title
   - Company name
   - Location
   - Work mode (onsite / hybrid / remote)
   - Salary or salary range (if listed)
   - Seniority level (junior / mid / senior / lead)
   - Employment type (full-time, contract, etc.)
   - How recently the job was posted

   **B. Key Responsibilities**
   - Responsibilities listed explicitly


   **C. Required Skills (Primary Requirements)**
   - Technical skills (e.g., Python, SQL, ML, cloud, statistics)
   - Domain-specific skills (e.g., finance, health, retail)
   - Experience level or years required

   **D. Secondary / Nice-to-Have Requirements**
   - Preferred skills, extra tools or frameworks
   - Desirable domain experience
   - Soft skills

   **E. Tools, Technologies, and Methods Mentioned**
   - Programming languages
   - ML frameworks + libraries
   - Cloud platforms
   - Data tools / visualization tools
   - MLOps / deployment requirements

   **F. Company Background**
   - Company description
   - Industry and size (if available)
   - Culture, values, mission (explicit or inferred)
   - Recent news or notable context (only from the job posting, do not search further)

4. Present all information clearly and neatly so the user can quickly understand the role. 

   Current date: {datetime.datetime.now().strftime("%Y-%m-%d")}
""",
    sub_agents=[robust_data_scientist_searcher],
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
