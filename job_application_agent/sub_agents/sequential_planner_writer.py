from google.adk.agents import SequentialAgent
from ..config import config
from .cover_letter_planner import cover_letter_planner
from .cover_letter_writer import cover_letter_writer

sequential_planner_writer = SequentialAgent(
    name="sequential_planner_writer",
    sub_agents=[cover_letter_planner, cover_letter_writer],
    description = "A sub-agent that first plans and then writes a cover letter for a job application.",
    
)