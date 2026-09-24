# Fast Chatt — 🤖 میرا پہلا AI چیٹ بوٹ

A simple AI chat bot built with **Streamlit**, **Python**, and **Google Gemini**.

## Requirements

- Python 3.9+ (this project was tested with Python 3.13)
- A Google Gemini API key — get one from the [Google AI Studio](https://aistudio.google.com/apikey)

## Setup

1. Open your terminal in this folder:

   ```bash
   cd D:\fast_chatt
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

3. Install the dependencies:

   ```bash
   pip install streamlit google-genai
   ```

## Add your API key

Set your Gemini API key as an environment variable (never hardcode it in the file):

- Windows (PowerShell):

  ```powershell
  $env:GEMINI_API_KEY = "your-api-key-here"
  ```

- macOS/Linux:

  ```bash
  export GEMINI_API_KEY="your-api-key-here"
  ```

## Run the project

```bash
streamlit run app.py
```

Your browser should open automatically at `http://localhost:8501`. If it does not, open that URL manually.