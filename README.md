# LLM Dataset Generator

Generate synthetic instruction-style datasets using Groq’s OpenAI-compatible API, with a Gradio web UI.

## Features
- Groq API integration via OpenAI wrapper
- Gradio UI for dataset generation
- Prompt-driven synthetic data generation
- Validation and filtering for SEO-style samples

## Requirements
- Python 3.10+
- A Groq API key

## Quick Start
1. **Clone and enter the project**
2. **Create a virtual environment**
	- Windows PowerShell:
	  - `python -m venv .venv`
	  - `.venv\Scripts\Activate.ps1`
3. **Install dependencies**
	- `pip install -r requirements.txt`
4. **Set environment variables**
	- Create `.env` from `.env.example`:
	  - `GROQ_API_KEY=your_groq_api_key_here`
5. **Run the UI**
	- `python app.py`
	- Open the Gradio link shown in the terminal.

## Project Structure
- `app.py` — Gradio UI entry point
- `src/generator.py` — Groq client + generation logic
- `src/validator.py` — Validation and filtering
- `src/exporter.py` — JSON/CSV exporters
- `src/prompts.py` — Prompt templates
- `data/` — Output datasets (if present)

## Configuration
Environment variables (see `.env.example`):
- `GROQ_API_KEY` — Required for Groq API access

## Notes
- If output is empty, check the validator rules in `src/validator.py` and ensure the model response matches the expected JSON format.
- For Groq via OpenAI wrapper, the base URL is `https://api.groq.com/openai/v1`.

## Common Commands
- Run UI: `python app.py`
- Update deps: `pip install -r requirements.txt`
