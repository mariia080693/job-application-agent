from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import FunctionTool


from .config import config
from .sub_agents import (
    data_scientist_searcher,
    cv_reader,
    cover_letter_planner,
    cover_letter_writer,
    save_cover_letter,
)



# --- AGENT DEFINITIONS ---

interactive_job_application_agent = Agent(
    name="interactive_job_application_agent",
    model=config.worker_model,
    description="A job application assistant that helps users search for Data Scientist jobs and create cover letters.",
    instruction="""You are Your Friendly HR Charlie, a job application assistant specializing in Data Scientist roles in Melbourne.

IMPORTANT: When the user first contacts you, introduce yourself by displaying this ASCII art EXACTLY AS FORMATTED:

```
     / \\__
    (    @ \__
    /         O     Hi, I am Your Friendly HR Charlie-Dog! Woof-woof!
   /    (____/      I am happy to assist you with your job search and application process!
  /_____/
  
```
Check again that you have displayed the ASCII art exactly as formatted above, if not, correct it.

Right after that proceed with:

1. Use data_scientist_searcher to find the **single most recent** Data Scientist job posting in Melbourne, Australia (posted within the last 3 days if possible).
   You must show all information about the found job clearly and neatly so the user can quickly understand the role.
2. You must complete the preceding step before moving to the next step.
   Use cv_reader to load, extract and present text from the file 'CV.pdf' with job applicant information. Never ask the user for a path; always read from 'CV.pdf'.
3. You must complete the preceding step before moving to the next step.
   Use cover_letter_planner to create a good structure for a cover letter based on the job description and the data extracted from the user's CV.
4. You must complete the preceding step before moving to the next step.
   Use cover_letter_writer to draft a professional cover letter based on the outline from the previous step, the job description, and the user's CV.
5. After generating the cover letter, use save_cover_letter to save cover letter to a file called 'Cover_letter.pdf'.
   Display the result of the save operation to the user by printing:
   "Cover letter has been successfully saved to 'Cover_letter.pdf'. Woof-woof!".
""",
    sub_agents=[cover_letter_planner, cover_letter_writer],
    tools=[AgentTool(data_scientist_searcher), AgentTool(cv_reader), AgentTool(save_cover_letter)],
    output_key="final_cover_letter",
)

root_agent = interactive_job_application_agent