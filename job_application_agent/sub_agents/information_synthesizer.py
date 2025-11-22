from google.adk.agents import Agent
from ..config import config

INFORMATION_SYNTHESIZER_INSTRUCTION = """
You are an information synthesizer.
Your goal is to collect information about a job posting and present it to the user in a clear and concise form.
You are given the {key_requirements}, {secondary_requirements}, and {company_culture} information about the job posting.
You need to synthesize this information into a summary that is easy to read and understand.
Output your summary as 'job_info'.
"""

information_synthesizer = Agent(
    name="information_synthesizer",
    model=config.worker_model,
    instruction=INFORMATION_SYNTHESIZER_INSTRUCTION,
    output_key="job_info",
)
