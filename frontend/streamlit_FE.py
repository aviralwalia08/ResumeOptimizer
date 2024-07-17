#!/usr/bin/env python
# coding: utf-8

# In[4]:


#pip install pdfplumber
#uploaded_resume_path = "C:/Users/Lenovo/Downloads/pt_restaurant(Sawan).pdf"  # Replace with the actual path to the uploaded resume
 #   optimized_resume_path = "C:/Users/Lenovo/Downloads/pt_grocery_warehouse_cashier(Sawan)_2[1].pdf"


# In[5]:


import streamlit as st
import spacy
import pandas as pd
import plotly.graph_objects as go
import pdfplumber
from io import BytesIO
import base64

# Custom CSS to improve the look of the app
st.markdown("""
    <style>
    .stFileUploader label, .stTextArea label {
        font-weight: bold;
        color: #2C3E50;
        font-size: 16px;
    }
    .stTextArea textarea {
        height: 150px; /* Adjusted height */
    }
    .stFileUploader .upload-drop {
        border: 2px dashed #3498DB;
        border-radius: 10px;
        background-color: #ECF0F1;
        padding: 10px;
        margin-top: 10px;
    }
    .stFileUploader:hover .upload-drop {
        border-color: #2980B9;
    }
    .stTextArea textarea {
        border: 2px solid #3498DB;
        border-radius: 10px;
        background-color: #ECF0F1;
        padding: 10px;
        margin-top: 10px;
    }
    .stButton button {
        background-color: #2ECC71;
        color: white;
        font-size: 16px;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        cursor: pointer;
        margin-top: 20px;
    }
    .stButton button:hover {
        background-color: #27AE60;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 1200px;
    }
    .box {
        border: 2px solid #d3d3d3;
        border-radius: 10px;
        padding: 10px;
        margin-top: 10px;
        background-color: #f8f8f8;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .box-header {
        font-weight: bold;
        color: #34495E;
        margin-bottom: 10px;
    }
    .table-container {
        margin-top: 10px;
        margin-bottom: 10px;
        width: 100%;
        background-color: #DFF0D8;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .footer {
        text-align: center;
        margin-top: 20px;
        color: #95a5a6;
    }
    .header {
        font-size: 28px;
        font-weight: bold;
        color: #2980B9;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .subheader {
        font-size: 22px;
        font-weight: bold;
        color: #2C3E50;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .highlight {
        background-color: #DFF0D8;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .highlight-header {
        color: #3C763D;
        font-weight: bold;
    }
    .circular-progress {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
""", unsafe_allow_html=True)

# Function to retrieve query parameters
params = st.experimental_get_query_params()

# Load Spacy model
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text)
    keywords = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return keywords

def create_circular_progress_bar(progress):
    fig = go.Figure(go.Pie(
        values=[progress, 100 - progress],
        hole=0.7,
        marker_colors=['#3498DB', '#E3F2FD'],
        textinfo='none'
    ))

    fig.add_annotation(
        text=f"{progress}%",
        x=0.5, y=0.5, showarrow=False,
        font_size=24,
        font_color="#2C3E50"
    )

    fig.update_layout(
        showlegend=False,
        margin=dict(t=0, b=0, l=0, r=0),
        height=200,
        width=200
    )
    
    return fig

# Function to generate a downloadable link for the optimized resume
def get_pdf_download_link(file_path, filename, text):
    with open(file_path, "rb") as f:
        file_data = f.read()
    b64 = base64.b64encode(file_data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}">{text}</a>'
    return href

def display_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Check if we are on the optimization results page
if params.get("page") == ["optimize_results"]:
    st.markdown('<div class="header">📝 Optimized Resume</div>', unsafe_allow_html=True)

    # Paths to the uploaded and optimized resume PDF files
    uploaded_resume_path = "C:/Users/avira/OneDrive - Trent University/Desktop/Final Project/sample_res.pdf"  # Replace with the actual path to the uploaded resume
    optimized_resume_path = "C:/Users/avira/OneDrive - Trent University/Desktop/Final Project/sample_res.pdf"   # Replace with the actual path to the optimized resume

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown('<div class="subheader">Uploaded Resume</div>', unsafe_allow_html=True)
        display_pdf(uploaded_resume_path)

        st.markdown('<div class="subheader">Current Progress</div>', unsafe_allow_html=True)
        st.markdown('<div class="circular-progress">', unsafe_allow_html=True)
        progress = 85  # Example optimized progress percentage
        st.plotly_chart(create_circular_progress_bar(progress), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="subheader">Additional Details</div>', unsafe_allow_html=True)
        st.write("Details about the optimization process or suggestions can go here.")
        
    with col2:
        st.markdown('<div class="subheader">Optimized Resume</div>', unsafe_allow_html=True)
        display_pdf(optimized_resume_path)
        st.markdown(get_pdf_download_link(optimized_resume_path, 'optimized_resume.pdf', '📥 Download Optimized Resume'), unsafe_allow_html=True)
    
    # Back button
    if st.button("Back", key="back"):
        st.experimental_set_query_params(page="results")
        st.experimental_rerun()

# Check if we are on the results page
elif params.get("page") == ["results"]:
    resume_text = params.get("resume_text", [""])[0]
    job_desc_text = params.get("job_desc_text", [""])[0]

    st.markdown('<div class="header">📊 Results and Suggestions</div>', unsafe_allow_html=True)
    st.write("Here are the results based on your uploaded resume and job description.")

    # Example data - in a real application, this would be dynamically generated
    progress = 65  # Example progress percentage
    top_keywords = ["Python", "Data Analysis", "SQL", "Machine Learning", "NLP", "Pandas", "NumPy", "Deep Learning", "Data Visualization", "Statistics"]
    keywords_matched = ["Python", "Data Analysis", "SQL", "Machine Learning"]
    keywords_missing = ["NLP", "Pandas", "NumPy", "Deep Learning", "Data Visualization", "Statistics"]
    hard_skills = ["Python", "Data Analysis", "SQL"]
    soft_skills = ["Communication", "Teamwork", "Problem-solving"]
    
    # Divide the page into two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="subheader">Current Progress</div>', unsafe_allow_html=True)
        st.markdown('<div class="circular-progress">', unsafe_allow_html=True)
        st.plotly_chart(create_circular_progress_bar(progress), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="subheader">Top 10 Keywords in Job Description</div>', unsafe_allow_html=True)
        top_keywords_df = pd.DataFrame(top_keywords, columns=["Keywords"])
        st.markdown('<div class="table-container">', unsafe_allow_html=True)
        st.dataframe(top_keywords_df)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="subheader">Keywords Matched</div>', unsafe_allow_html=True)
        st.markdown('<div class="box highlight"><div class="highlight-header">Matched Keywords</div>' + '<br>'.join(keywords_matched) + '</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="subheader">Keywords Missing</div>', unsafe_allow_html=True)
        st.markdown('<div class="box highlight"><div class="highlight-header">Missing Keywords</div>' + '<br>'.join(keywords_missing) + '</div>', unsafe_allow_html=True)

        st.markdown('<div class="subheader">Hard Skills</div>', unsafe_allow_html=True)
        st.markdown('<div class="box highlight">' + '<br>'.join(hard_skills) + '</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="subheader">Soft Skills</div>', unsafe_allow_html=True)
        st.markdown('<div class="box highlight">' + '<br>'.join(soft_skills) + '</div>', unsafe_allow_html=True)

        if st.button("Optimize"):
            st.experimental_set_query_params(page="optimize_results")
            st.experimental_rerun()

    if st.button("Back", key="back"):
        st.experimental_set_query_params(page="")
        st.experimental_rerun()

else:
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






