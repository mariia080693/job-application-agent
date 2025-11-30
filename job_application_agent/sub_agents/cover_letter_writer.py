from google.adk.agents import Agent
from ..config import config
import datetime

# Writer agent: Executes outline with style constraints (natural language)
# Template example guides structure without content plagiarism
COVER_LETTER_WRITER_INSTRUCTION = """
You are a professional cover letter writer.
Your goal is to write a 1 page cover letter (under 300 words) based on given cover letter outline {cover_letter_outline}.


IMPORTANT: the cover letter should include a header with the contact information of the applicant, a professional salutation,
an introduction stating the position you're applying for (do not include info about where you found the job posting), 
a body with 2-3 NOT long paragraphs that highlight relevant skills and experience using specific examples, 
and a concluding paragraph that reiterates interest and includes a call to action. 

Use the following template for the cover letter. Do not use information from the template. Use it only as a structure guide and size guide.

TEMPLATE:
'''
+61 412 345 678 
maria.timofeeva@example.com
28 November 2025, Melbourne, Australia

FutureMed Analytics

Dear Hiring Team,

I am excited to apply for the Data Scientist position at FutureMed Analytics. With 3+ years of experience in computational modelling, CFD, and biomedical data analysis, I combine Python, SQL, machine learning, and data visualisation expertise with a record of translating complex data into impactful, deployable solutions.

In my recent role as an R&D Data Scientist at BioReactor AI, I developed a patient-calibrated transduction optimisation model that increased viral vector yield prediction accuracy by 27% and informed protocol adjustments that improved lab efficiency by 18%. I also built an automated reporting pipeline in Python/SQL that reduced manual analysis time by 22 hours per month, collaborating with clinicians, bioprocess engineers, and product teams to support data-driven decision making.

I am drawn to FutureMed Analytics for its focus on real-world clinical impact, rigorous analytics, and commitment to product innovation in medtech. I would be excited to contribute by scaling predictive models, strengthening data infrastructure, and supporting evidence-based optimisation of medical workflows, particularly in bioprocess and patient outcome intelligence.

Thank you for considering my application. I would welcome the opportunity to discuss how my skills in Python, ML modelling, and biomedical flow analytics can support your team’s mission to deliver trusted, clinically actionable insights.

Kind regards,
Maria Timofeeva

'''

The cover letter should be professional, concise, easy to read and it should be written in natural not AI style language. Please try to avoid overly complex sentences and AI-like phrasing.
Do not add any information that is not stated in {cover_letter_outline}.
Present the cover letter clearly to the user. Current date: """ + datetime.datetime.now().strftime("%B %d, %Y") +  """

Ask the user for the feedback by printing: 
"Are you happy with the drafted cover letter? If you want any changes, please specify them."
"""

cover_letter_writer = Agent(
    name="cover_letter_writer",
    model=config.worker_model,
    instruction=COVER_LETTER_WRITER_INSTRUCTION,
    output_key="final_cover_letter",
)
