import google.generativeai as genai

# Setup
genai.configure(api_key="AIzaSyAghpmwB7XpUUl5o7H2Vpdlj0o4vFF4zr8")

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_ai_feedback(resume_text):
    prompt = (
        "You are an AI Resume Expert. Analyze the following resume and give detailed feedback on formatting, clarity, achievements, impact, and suggestions for improvement:\n\n"
        + resume_text
    )
    response = model.generate_content(prompt)
    return response.text
