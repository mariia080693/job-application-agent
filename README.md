# Job Application Agent 🐕

An intelligent AI-powered assistant that helps job seekers search for Data Scientist positions in Melbourne, Australia and create tailored cover letters. Meet Charlie-Dog, your friendly HR assistant!

## 🌟 Features

- **Automated Job Search**: Searches for the most recent Data Scientist job posting in Melbourne, Australia (within the last 7 days)
- **Comprehensive Job Analysis**: Extracts detailed job information including responsibilities, required skills, company background, and more
- **CV Analysis**: Extracts and analyzes information from your CV (PDF format) and presents it in a well-structured format
- **Cover Letter Planning**: Creates structured outlines for cover letters based on job requirements and your CV
- **Cover Letter Writing**: Generates professional, personalized cover letters
- **Iterative Refinement**: Review and revise both job postings and cover letters based on your feedback
- **PDF Export**: Saves your cover letter as a PDF file with proper character encoding

## 🏗️ Project Structure

```
job-application-agent/
├── requirements.txt              # Project dependencies
├── job_application_agent/
│   ├── __init__.py              # Package initialization
│   ├── agent.py                 # Main agent orchestration
│   ├── config.py                # Configuration settings
│   ├── tools.py                 # Utility functions (CV reading, PDF saving)
│   └── sub_agents/              # Specialized sub-agents
│       ├── __init__.py
│       ├── data_scientist_searcher.py    # Job search agent
│       ├── cv_reader.py                  # CV extraction agent
│       ├── cover_letter_planner.py       # Cover letter outline agent
│       ├── cover_letter_writer.py        # Cover letter writing agent
│       ├── sequential_planner_writer.py  # Sequential planner + writer agent
│       └── save_cover_letter.py          # PDF saving agent
```

## 📋 Prerequisites

- Python 3.8+
- Google Cloud Platform account (for Vertex AI) or Google API key
- A CV file named `CV.pdf` in the project directory

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/mariia080693/job-application-agent.git
cd job-application-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up authentication:

**Option A: Using Vertex AI (recommended)**
- Set up [Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials)
- Ensure `GOOGLE_GENAI_USE_VERTEXAI=True` in your `.env` file (or leave unset, as this is the default)

**Option B: Using API Key**
- Create a `.env` file in the project root
- Add your Google API key:
```
GOOGLE_GENAI_USE_VERTEXAI=False
GOOGLE_API_KEY=your_api_key_here
```

4. Place your CV:
- Save your CV as `CV.pdf` in the project root directory (use my CV as an example)

## 💻 Usage

Start the interactive agent:
```bash
adk web
```

The agent will guide you through the following steps:

1. **Introduction**: Meet Charlie-Dog, your friendly HR assistant (displays ASCII art greeting)
2. **Job Search**: Automatically finds the most recent Data Scientist job in Melbourne posted within the last 7 days
3. **Job Review**: Review the comprehensive job posting (including overview, responsibilities, required skills, company background) and provide feedback. The agent will search for another job if you're not satisfied
4. **CV Analysis**: The agent reads `CV.pdf` and presents your information in a well-structured format
5. **Cover Letter Planning**: Creates a structured outline for your cover letter based on job requirements and your CV
6. **Cover Letter Writing**: Drafts a professional cover letter (under 300 words) with proper formatting including header, salutation, and call to action
7. **Revision**: Provide feedback and request changes if needed. The agent will revise based on your input
8. **Save Confirmation**: Decide whether to save the cover letter
9. **Save**: Saves the final cover letter as `Cover_letter.pdf` with proper character encoding


## 🤖 Agent Architecture

The system uses a hierarchical agent structure with specialized sub-agents:

### Root Agent: `interactive_job_application_agent`
- Orchestrates the entire workflow and manages user interaction
- Presents Charlie-Dog ASCII art greeting
- Handles feedback loops for job satisfaction and cover letter revisions
- Manages the sequential flow from job search to cover letter saving

### Sub-Agents:
1. **data_scientist_searcher** (LlmAgent): 
   - Searches for the most recent Data Scientist job posting in Melbourne using Google Search
   - Extracts comprehensive job information organized into sections: Job Overview, Key Responsibilities, Required Skills, Secondary Requirements, and Company Background
   
2. **cv_reader** (Agent): 
   - Reads `CV.pdf` using the `read_cv` tool (powered by pdfplumber)
   - Transforms raw CV content into a clean, well-structured format with clear sections
   
3. **sequential_planner_writer** (SequentialAgent): 
   - Orchestrates the sequential execution of cover letter planning and writing
   - Sub-agents:
     - **cover_letter_planner**: Compares job requirements with CV content and creates a structured outline
     - **cover_letter_writer**: Generates a professional cover letter (under 300 words) based on the outline, following a specific template structure
   
4. **save_cover_letter** (Agent): 
   - Uses the `save_cover_letter_to_file` tool to save the cover letter as PDF
   - Handles character encoding to ensure special characters are properly converted

## 👥 Author

Maria Timofeeva - [mariia080693](https://github.com/mariia080693)

## 🔑 Key Implementation Details

### Models Used
- **Primary Model**: `gemini-2.5-flash` (configurable in `config.py`)
- All agents use the same model for consistency

### Tools and Functions
- **Google Search**: Integrated via ADK for job searching
- **read_cv**: Uses pdfplumber for better PDF text extraction with structure preservation
- **save_cover_letter_to_file**: Uses FPDF library with automatic character encoding handling

### Agent Types
- **Agent**: Standard agent with tools (cv_reader, save_cover_letter)
- **LlmAgent**: Agent optimized for LLM tasks (data_scientist_searcher)
- **SequentialAgent**: Orchestrates multiple agents in sequence (sequential_planner_writer)

---

**Note**: This agent is specifically designed for Data Scientist job searches in Melbourne, Australia. The workflow can be adapted for other roles and locations.
