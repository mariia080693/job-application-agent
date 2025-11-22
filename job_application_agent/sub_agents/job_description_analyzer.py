# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.agents import Agent
from ..config import config

KEY_REQUIREMENTS_INSTRUCTION = """
You are a job description analyzer.
Your goal is to identify the key requirements mentioned in a job posting.
You are given a job posting: {job_postings} to do this.
You need to extract the key skills, experience, and qualifications required for the job.
"""

SECONDARY_REQUIREMENTS_INSTRUCTION = """
You are a job description analyzer.
Your goal is to identify the secondary requirements mentioned in a job posting.
You are given a job posting: {job_postings} to do this.
You need to extract the nice-to-have skills, experience, and qualifications for the job.
"""

COMPANY_CULTURE_INSTRUCTION = """
You are a job description analyzer.
Your goal is to identify important information about the company culture and work environment.
You are given a job posting: {job_postings} to do this.
You need to extract information about the company's values, mission, team structure, and any other relevant details about the work environment.
"""

key_requirements_analyzer = Agent(
    name="key_requirements_analyzer",
    model=config.worker_model,
    instruction=KEY_REQUIREMENTS_INSTRUCTION,
    output_key="key_requirements",
)

secondary_requirements_analyzer = Agent(
    name="secondary_requirements_analyzer",
    model=config.worker_model,
    instruction=SECONDARY_REQUIREMENTS_INSTRUCTION,
    output_key="secondary_requirements",
)

company_culture_analyzer = Agent(
    name="company_culture_analyzer",
    model=config.worker_model,
    instruction=COMPANY_CULTURE_INSTRUCTION,
    output_key="company_culture",
)
