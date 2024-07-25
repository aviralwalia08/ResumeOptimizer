# optimization_results_page.py

import streamlit as st
import difflib
import plotly.graph_objects as go
import base64
from src.overall_edition import *
from src.suggestions_resume import *

industry = 'Data Science'
Job_Profile = 'Data Scientist'

def highlight_differences(text1, text2):
    matcher = difflib.SequenceMatcher(None, text1.split(), text2.split())
    highlighted_text1 = []
    highlighted_text2 = []
    
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            highlighted_text1.extend(text1.split()[i1:i2])
            highlighted_text2.extend(text2.split()[j1:j2])
        elif tag == 'replace':
            highlighted_text1.extend([f"<span style='background-color: pink;'>{word}</span>" for word in text1.split()[i1:i2]])
            highlighted_text2.extend([f"<span style='background-color: lightgreen;'>{word}</span>" for word in text2.split()[j1:j2]])
        elif tag == 'delete':
            highlighted_text1.extend([f"<span style='background-color: red;'>{word}</span>" for word in text1.split()[i1:i2]])
        elif tag == 'insert':
            highlighted_text2.extend([f"<span style='background-color: lightgreen;'>{word}</span>" for word in text2.split()[j1:j2]])
    
    return " ".join(highlighted_text1), " ".join(highlighted_text2)

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

def get_txt_download_link(file_data, filename, text):
    b64 = base64.b64encode(file_data.encode()).decode()
    href = f'<a href="data:text/plain;base64,{b64}" download="{filename}">{text}</a>'
    return href

def display_txt(file_path):
    with open(file_path, "r") as f:
        return f.read()

def display_optimization_results_page(resume_text_new,job_desc_text_new):
    st.markdown('<div class="header">📝 Optimized Resume</div>', unsafe_allow_html=True)

    # uploaded_resume_path = "C:/Users/avira/OneDrive - Trent University/Desktop/Final Project/demo.txt"
    # optimized_resume_path = "C:/Users/avira/OneDrive - Trent University/Desktop/Final Project/demo2.txt"

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="subheader">Uploaded Resume</div>', unsafe_allow_html=True)
        # uploaded_resume_text = display_txt(uploaded_resume_path)
        # optimized_resume_text = display_txt(optimized_resume_path)

        uploaded_resume_text = resume_text_new

        updated_res = overall_edit(industry,Job_Profile,job_desc_text_new,uploaded_resume_text)
        optimized_resume_text = updated_res[0]['Updated_Resume']

        # print(type(uploaded_resume_text),type(optimized_resume_text))
        # print('#####################################',uploaded_resume_text,'-----------------------------------------------',optimized_resume_text,'===============',job_desc_text_new)


        highlighted_text1, highlighted_text2 = highlight_differences(resume_text_new, optimized_resume_text)
        st.markdown(f"""<div class="box">{highlighted_text1.replace('/n', '<br>')}</div>""", unsafe_allow_html=True)
        
        st.markdown('<div class="subheader">New Alignment Score</div>', unsafe_allow_html=True)
        st.markdown('<div class="circular-progress">', unsafe_allow_html=True)
        progress = 85 # change this down the line
        st.plotly_chart(create_circular_progress_bar(progress), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="subheader">Optimized Resume</div>', unsafe_allow_html=True)
        st.markdown(f"""<div class="box">{highlighted_text2.replace('/n', '<br>')}</div>""", unsafe_allow_html=True)

        st.markdown('<div class="subheader">Suggestions</div>', unsafe_allow_html=True)
        sug = suggestions_task(job_desc_text_new,optimized_resume_text)
        suggest = sug[0]['Suggestions']
        st.write(suggest)
    
    st.markdown(f'<div style="text-align: center;">{get_txt_download_link(optimized_resume_text, "optimized_resume.txt", "📥 Download Optimized Resume")}</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <style>
        .center-button {
            display: flex;
            justify-content: center;
        }
        </style>
        <div class="center-button">
    """, unsafe_allow_html=True)

    if st.button("Back", key="back"):
        st.experimental_set_query_params(page="results")
        st.experimental_rerun()

    st.markdown("</div>", unsafe_allow_html=True)
