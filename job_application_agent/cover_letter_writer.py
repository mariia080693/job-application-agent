from job_application_agent.agent import interactive_job_application_agent


if __name__ == "__main__":
    # The user can provide a prompt to the agent before the conversation starts.
    # The agent will use this prompt as the first turn of the conversation.
    # If no prompt is provided, the agent will start the conversation with a
    # default message.
    interactive_job_application_agent.run(
        prompt="Please find the best job for me and write a cover letter using my CV."
    )
