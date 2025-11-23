from google.adk.agents import Agent, LoopAgent
from google.adk.tools import google_search

from ..validation_checkers import SearchValidationChecker
from ..config import config
from ..agent_utils import suppress_output_callback

data_scientist_searcher = Agent(
    name="data_scientist_searcher",
    model=config.worker_model,
    instruction="""
    Search for just one recent 'Data scientist' job posting in Melbourne (posted within the last 3 days if possible), Australia. Find just one relevant job posting.
    
    Retrieve and present **all information** from the job posting. 
    Your goal is to extract *comprehensive, structured* details — not just surface-level text.

    In your output, clearly present the information with the following sections:

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
    - Technical skills including programming languages, ML/AI frameworks, cloud platforms, and data tools (e.g., Python, SQL, ML, AWS, PowerBI, etc.). List names of the tools/frameworks.
    - Domain-specific skills (e.g., finance, health, retail)
    - Experience level or years required

    **D. Secondary / Nice-to-Have Requirements**
    - Preferred skills, extra tools or frameworks
    - Desirable domain experience
    - Soft skills (e.g., communication, teamwork)

    **E. Company Background**
    - Company description
    - Industry and size (if available)
    - Culture, values, mission (explicit or inferred)

    Present all information clearly and neatly so the user can quickly understand the role. 
    """,
    tools=[google_search],
    output_key="job_postings",
    #after_agent_callback=suppress_output_callback,
)

robust_data_scientist_searcher = LoopAgent(
    name="robust_data_scientist_searcher",
    description="A robust data science seracher that retries if it fails.",
    sub_agents=[
        data_scientist_searcher,
        SearchValidationChecker(name="search_validation_checker"),
    ],
    max_iterations=1,
    after_agent_callback=suppress_output_callback,
)
