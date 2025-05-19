import os
import google.generativeai as genai
from dotenv import load_dotenv

# upload .env file
load_dotenv()

# Get API key from environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini model description
model = genai.GenerativeModel("gemini-1.5-flash")

def explain_failure(test_name: str, error_message: str) -> str:
    prompt = f"""
    A unit test in Python has failed.

    Test name: {test_name}
    Erorr message: {error_message}

   Please provide a technical analysis of why this test might have failed and suggest possible fixes.
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"[Gemini AI explanation failed: {str(e)}]"



