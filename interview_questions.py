from gemini_api import model

def generate_questions(resume_text):
    prompt = (
        "Generate 5 technical and behavioral interview questions based on this resume:\n\n"
        + resume_text
    )
    response = model.generate_content(prompt)
    return response.text.strip().split("\n")
