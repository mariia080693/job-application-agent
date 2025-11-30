from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from job_application_agent.tools import save_cover_letter_to_file
from ..config import config
import datetime

# Hardcoded filename ('Cover_letter.pdf') for consistent output location
SAVE_COVER_LETTER_INSTRUCTION = """
Use save_cover_letter_to_file to save cover letter from {final_cover_letter} to a file called 'Cover_letter.pdf'. Do not ask for user confirmation. Do not ask user to specidy a file name, it should be always 'Cover_letter.pdf'.
Make sure to pass the complete cover letter text to the save function.
"""

save_cover_letter = Agent(
    name="save_cover_letter",
    model=config.worker_model,
    instruction=SAVE_COVER_LETTER_INSTRUCTION,
    tools=[FunctionTool(save_cover_letter_to_file)],
)