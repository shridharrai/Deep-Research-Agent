---
title: deep_research
app_file: app.py
sdk: gradio
sdk_version: 6.14.0
---

# Deep Research

Deep Research is a Gradio-based AI research assistant that turns a user question into a polished research report. It uses multiple agent roles to plan searches, gather information, write a report, and optionally send that report by email.

## What it does

When you enter a research question, the app:

1. Creates a search plan
2. Runs several web-search-based research steps
3. Writes a detailed markdown report
4. Sends the report via email (or pushes it to Pushover when email is disabled)

## Project structure

- app.py: Gradio UI entry point
- research_manager.py: orchestrates the end-to-end research workflow
- planner_agent.py: creates the list of search queries
- search_agent.py: performs individual web searches and summarizes findings
- writer_agent.py: generates the final markdown report
- email_agent.py: formats and sends the report
- messenger.py: email and Pushover delivery helpers

## Requirements

- Python 3.12+
- An OpenAI API key
- Internet access for web research

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Or with uv:

```bash
uv sync
```

Create a .env file with the required environment variables:

```bash
OPENAI_API_KEY=your_openai_api_key
DEFAULT_MODEL_NAME=gpt-5.4-mini
HOW_MANY_SEARCHES=3
USE_EMAIL=true
```

Optional email configuration:

```bash
EMAIL_ADDRESS=your_email@example.com
EMAIL_SMTP_SERVER=smtp.example.com
EMAIL_APP_PASSWORD=your_app_password
```

Optional Pushover fallback:

```bash
PUSHOVER_USER=your_pushover_user
PUSHOVER_TOKEN=your_pushover_token
```

## Run the app

```bash
uv run app.py
```

The app will launch in your browser with a simple input box for your research question.

## Notes

- The default model can be changed with DEFAULT_MODEL_NAME.
- HOW_MANY_SEARCHES controls how many search topics the planner generates.
- If USE_EMAIL is set to false, the report is pushed to Pushover instead of being emailed.
