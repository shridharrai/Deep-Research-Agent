from agents import Agent, function_tool, ModelSettings
from messenger import send_email, push
from dotenv import load_dotenv
import os

load_dotenv(override=True)

MODEL_NAME = os.getenv("DEFAULT_MODEL_NAME", "gpt-5.4-mini")
USE_EMAIL = os.getenv("USE_EMAIL", "true").lower() == "true"

settings = ModelSettings(tool_choice="required")
INSTRUCTIONS = """
You are provided with a detailed report. Use your tool to send an email, converting the report into
a clean, well presented HTML email with an appropriate subject line.
"""


@function_tool
def send_email_tool(subject: str, text_body: str, html_body: str) -> str:
    """
    Send out an email with the given subject and body

    Args:
        subject: The subject of the email
        text_body: The body of the email as plain text
        html_body: The HTML body of the email
    """

    if USE_EMAIL:
        send_email(subject, text_body, html_body)
    else:
        push(f"Subject: {subject}\n\n{text_body}")

    return "Email Sent Successfully"


email_agent = Agent(
    name="Email Agent",
    instructions=INSTRUCTIONS,
    model=MODEL_NAME,
    tools=[send_email_tool],
    model_settings=settings,
)
