from google.adk.agents import Agent
from ..config import config

COVER_LETTER_PLANNER_INSTRUCTION = """
You are a cover letter planner.
Your goal is to create a good structure for a cover letter based on the job description and the data extracted from the user's CV.
You have two inputs:
-  synthesized job description information (from the data_scientist_searcher agent)
- the user's CV information (from the read_cv tool)
You need to compare the information and outline a cover letter structure that highlights the user's skills and experience that are most relevant to the job.
The outline should be a list of key points to be included in the cover letter.
Present the outline clearly to the user.
"""

cover_letter_planner = Agent(
    name="cover_letter_planner",
    model=config.worker_model,
    instruction=COVER_LETTER_PLANNER_INSTRUCTION,
)
