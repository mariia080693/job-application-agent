from google.adk.agents import Agent, LoopAgent
from google.adk.tools import google_search

from ..validation_checkers import SearchValidationChecker
from ..config import config
from ..agent_utils import suppress_output_callback

data_scientist_searcher = Agent(
    name="data_scientist_searcher",
    model=config.worker_model,
    instruction="""
    Search for the recent 'Data scientist' job posting in Melbourne, Australia. Find just one relevant job posting.
    Show all the details of the job description.
    Format your output clearly so all the job information can be easily identified.
    The information should include (if available) company name, location, salary, requirements, and detailed job description.
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
