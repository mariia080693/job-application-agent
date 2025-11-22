
import os
from dataclasses import dataclass
from dotenv import load_dotenv
import google.auth

load_dotenv()

if os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "True").lower() == "true":
    try:
        _, project_id = google.auth.default()
        os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
        os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
    except google.auth.exceptions.DefaultCredentialsError:
        print(
            "Authentication failed. Please configure your environment with Application Default Credentials."
        )
        # Handle the error appropriately, e.g., by exiting or using a fallback.
        project_id = None
else:
    # When using an API key, a project ID is not required.
    # The GOOGLE_API_KEY is loaded from the .env file by load_dotenv().
    if not os.getenv("GOOGLE_API_KEY"):
        print(
            "GOOGLE_API_KEY not found. Please set it in your .env file when GOOGLE_GENAI_USE_VERTEXAI is False."
        )


@dataclass
class JobApplicationConfig:
    """Configuration for the job application agent."""

    worker_model: str = "gemini-2.5-flash"
    max_search_iterations: int = 5


config = JobApplicationConfig()
