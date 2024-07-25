# initial_upload_page.py

import streamlit as st
from src.utils import *
import warnings

# Suppress specific warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def display_initial_upload_page():
    st.markdown('<div class="header">📄 Resume Optimizer</div>', unsafe_allow_html=True)
    st.write("Upload your resume and job description to see the match percentage and get suggestions for improvements.")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="subheader">Resume</div>', unsafe_allow_html=True)
        resume_text = st.text_area("Copy and paste resume...")
        resume_file = st.file_uploader("Drag-n-drop or upload your resume", type=["pdf"], key="resume")

    with col2:
        st.markdown('<div class="subheader">Job Description</div>', unsafe_allow_html=True)
        job_desc_text = st.text_area("Copy and paste job description...")
        job_desc_file = st.file_uploader("Drag-n-drop or upload job description", type=["pdf"], key="job_desc")

    if st.button("Submit"):
        if resume_file is not None:
            resume_text = input_pdf_text(resume_file)
            resume_text = f"""{str(resume_text)}"""

        if job_desc_file is not None:
            job_desc_text = input_pdf_text(job_desc_file)
            job_desc_text = f"""{str(job_desc_text)}"""

        if (resume_text != "") & (job_desc_text != ""):
            # print('################ part 1 ########################')
            # print(resume_text)
            # print('========')
            # print(job_desc_text)
            # print('################part 1 close########################')
            st.experimental_set_query_params(page="results", resume_text=resume_text, job_desc_text=job_desc_text)
            # st.query_params.from_dict({page:"results", resume_text:resume_text, job_desc_text:job_desc_text})
            st.experimental_rerun()
        elif resume_text == "":
            st.info("Please upload the resume.", icon="⚠️")
        elif job_desc_text == "":
            st.info("Please upload the Job Description", icon="⚠️")
        

    st.info("Ensure your resume is updated with relevant keywords to improve your match percentage.")
    st.markdown('<div class="footer">Developed with ❤ by Aviral , Sawan & Sufyan . For the the students by the Students.</div>', unsafe_allow_html=True)
