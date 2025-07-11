import re

def generate_rule_based_feedback(text):
    feedback = []

    if len(text) < 100:
        feedback.append("Resume seems too short. Consider adding more experience or skills.")

    if "Objective" not in text and "Summary" not in text:
        feedback.append("Consider adding an Objective or Summary section.")

    if not re.search(r'\bPython|Java|C\+\+|JavaScript\b', text, re.I):
        feedback.append("Mention at least one programming language if applicable.")

    if "Intern" not in text:
        feedback.append("No internship experience found. If applicable, add it.")

    if not feedback:
        feedback.append("No major issues found. Good job!")

    return "\n".join(feedback)
