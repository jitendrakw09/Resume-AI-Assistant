import streamlit as st
from resume_parser import extract_text_from_pdf
from feedback_engine import generate_rule_based_feedback
from gemini_api import generate_ai_feedback
from interview_questions import generate_questions

st.set_page_config(page_title="Resume AI Assistant", layout="wide", page_icon="📄")

# Custom Header
st.markdown("""
    <style>
        .header {
            background-color: #007acc;
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 1rem;
        }
        .header h1 {
            color: white;
            font-size: 2.7rem;
            margin: 0;
        }
        .footer {
            margin-top: 3rem;
            text-align: center;
            font-size: 0.9rem;
            color: grey;
        }
        .css-1aumxhk {
            padding: 2rem;
        }
    </style>
    <div class="header">
        <h1>📄 Resume AI Assistant</h1>
    </div>
""", unsafe_allow_html=True)

st.sidebar.title("📁 Upload Resume")
uploaded_file = st.sidebar.file_uploader("Choose your PDF", type=["pdf"])

st.caption("An intelligent resume analyzer and interview question generator.")

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.success("✅ Resume uploaded and parsed successfully!")

    tab1, tab2, tab3, tab4 = st.tabs(["📄 Resume Text", "🤖 Gemini Feedback", "📏 Rule-Based Feedback", "💬 Interview Questions"])

    with tab1:
        st.subheader("📄 Extracted Resume Text")
        st.code(resume_text, language="markdown")

    with tab2:
        st.subheader("🤖 AI Feedback from Gemini")
        with st.spinner("Thinking..."):
            st.write(generate_ai_feedback(resume_text))

    with tab3:
        st.subheader("📏 Rule-Based Resume Feedback")
        st.markdown(generate_rule_based_feedback(resume_text))

    with tab4:
        st.subheader("💬 AI-Generated Interview Questions")
        questions = generate_questions(resume_text)
        for i, q in enumerate(questions, 1):
            st.markdown(f"**Q{i}.** {q}")
else:
    st.info("Upload your resume PDF using the sidebar to begin.")

# Clean Footer
st.markdown("""
    <div class="footer">
        A Project Made by Jitendra
    </div>
""", unsafe_allow_html=True)
