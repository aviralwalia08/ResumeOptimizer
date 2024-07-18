# wrapper.py

import streamlit as st
from initial_upload_page import display_initial_upload_page
# from results_page import display_results_page
from results_page import *
from optimization_results_page import display_optimization_results_page

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
        height: 400px;
        overflow-y: auto;
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

params = st.experimental_get_query_params()

if params.get("page") == ["optimize_results"]:
    display_optimization_results_page()
elif params.get("page") == ["results"]:
    resume_text = params.get("resume_text", [""])[0]
    job_desc_text = params.get("job_desc_text", [""])[0]
    display_results_page(resume_text, job_desc_text)
else:
    display_initial_upload_page()
