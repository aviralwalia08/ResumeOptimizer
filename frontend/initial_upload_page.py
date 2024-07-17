# initial_upload_page.py

import streamlit as st

def display_initial_upload_page():
    st.markdown('<div class="header">📄 Resume Optimizer</div>', unsafe_allow_html=True)
    st.write("Upload your resume and job description to see the match percentage and get suggestions for improvements.")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="subheader">Resume</div>', unsafe_allow_html=True)
        resume_text = st.text_area("Copy and paste resume...")
        resume_file = st.file_uploader("Drag-n-drop or upload your resume", type=["txt", "pdf", "docx"], key="resume")

    with col2:
        st.markdown('<div class="subheader">Job Description</div>', unsafe_allow_html=True)
        job_desc_text = st.text_area("Copy and paste job description...")
        job_desc_file = st.file_uploader("Drag-n-drop or upload job description", type=["txt", "pdf", "docx"], key="job_desc")

    if st.button("Submit"):
        st.experimental_set_query_params(page="results", resume_text=resume_text, job_desc_text=job_desc_text)
        st.experimental_rerun()

    st.info("Ensure your resume is updated with relevant keywords to improve your match percentage.")
    st.markdown('<div class="footer">Developed with ❤ by Your Name</div>', unsafe_allow_html=True)
