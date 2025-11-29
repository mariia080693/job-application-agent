# Job Application Agent 🐕

An intelligent AI-powered assistant that helps job seekers search for Data Scientist positions and create tailored cover letters. Meet Charlie-Dog, your friendly HR assistant!

## 🌟 Features

- **Automated Job Search**: Searches for recent Data Scientist job postings in Melbourne, Australia
- **CV Analysis**: Extracts and analyzes information from your CV (PDF format)
- **Cover Letter Planning**: Creates structured outlines for cover letters based on job requirements and your CV
- **Cover Letter Writing**: Generates professional, personalized cover letters
- **PDF Export**: Saves your cover letter as a PDF file
- **Interactive Workflow**: Guides you through the entire application process with feedback loops

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
- Save your CV as `CV.pdf` in the project root directory

## 💻 Usage

Start the interactive agent:
```bash
adk web
```

The agent will guide you through the following steps:

1. **Introduction**: Meet Charlie-Dog, your friendly HR assistant
2. **Job Search**: Automatically finds the most recent Data Scientist job in Melbourne
3. **Job Review**: Review the job posting and provide feedback
4. **CV Analysis**: The agent reads and presents your CV information
5. **Cover Letter Planning**: Creates a structured outline for your cover letter
6. **Cover Letter Writing**: Drafts a professional cover letter
7. **Revision**: Provide feedback and request changes if needed
8. **Save**: Option to save the final cover letter as `Cover_letter.pdf`

## 🛠️ Configuration

Edit `job_application_agent/config.py` to customize:

- `worker_model`: The AI model to use (default: "gemini-2.5-flash")
- `max_search_iterations`: Maximum number of search attempts (default: 5)

## 📦 Dependencies

- `google-adk==1.18.0` - Google AI Development Kit
- `pytest==8.4.2` - Testing framework
- `pytest-asyncio==1.2.0` - Async testing support
- `fpdf==1.7.2` - PDF generation
- `pdfplumber` - PDF text extraction
- `python-dotenv` - Environment variable management

## 🤖 Agent Architecture

The system uses a hierarchical agent structure:

### Root Agent: `interactive_job_application_agent`
Orchestrates the entire workflow and manages user interaction.

### Sub-Agents:
1. **data_scientist_searcher**: Searches for job postings using Google Search
2. **cv_reader**: Extracts and formats CV information from PDF
3. **cover_letter_planner**: Creates cover letter structure and outline
4. **cover_letter_writer**: Generates the final cover letter content
5. **save_cover_letter**: Saves the cover letter to PDF format

## 🔧 Troubleshooting

### Authentication Issues
- **Vertex AI**: Run `gcloud auth application-default login`
- **API Key**: Ensure your `.env` file contains a valid `GOOGLE_API_KEY`

### CV Not Found
- Ensure `CV.pdf` is in the project root directory
- Check file name matches exactly (case-sensitive)

### PDF Generation Errors
- The system automatically handles special characters and Unicode
- If issues persist, check the content for unsupported characters

## 📄 License

This project is part of the Google Kaggle AI Agent competition.

## 👥 Author

Maria Timofeeva - [mariia080693](https://github.com/mariia080693)
---

**Note**: This agent is specifically designed for Data Scientist job searches in Melbourne, Australia. The workflow can be adapted for other roles and locations by modifying the agent instructions.
