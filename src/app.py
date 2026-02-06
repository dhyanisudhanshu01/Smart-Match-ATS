import streamlit as st
from engine import extract_text_from_pdf, compute_similarity, gemini_gap_analysis

st.set_page_config(
    page_title="Smart-Match ATS",
    page_icon=":briefcase:",
    layout="centered",
)

st.title("💼 - Smart-Match ATS")
st.subheader("AI Resume Matcher")

uploaded_resume = st.file_uploader("Upload your resume (PDF format)", type=["pdf"])

job_description = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):
    if uploaded_resume and job_description:
        with st.spinner("Analyzing..."):
            resume_text = extract_text_from_pdf(uploaded_resume)
            similarity_score = compute_similarity(resume_text, job_description)
            feedback = gemini_gap_analysis(resume_text, job_description)

        st.metric("Match Score:", round(similarity_score, 2))
        st.subheader("Feedback:")
        st.markdown(feedback)

        
    else:
        st.error("Please upload a resume and paste a job description to analyze.")