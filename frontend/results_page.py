# results_page.py

import streamlit as st
import plotly.graph_objects as go
import pandas as pd

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

def display_results_page(resume_text, job_desc_text):
    st.markdown('<div class="header">📊 Results and Suggestions</div>', unsafe_allow_html=True)
    st.write("Here are the results based on your uploaded resume and job description.")

    # Example data - in a real application, this would be dynamically generated
    progress = 65  # Example progress percentage
    top_keywords = ["Python", "Data Analysis", "SQL", "Machine Learning", "NLP", "Pandas", "NumPy", "Deep Learning", "Data Visualization", "Statistics"]
    keywords_matched = ["Python", "Data Analysis", "SQL", "Machine Learning"]
    keywords_missing = ["NLP", "Pandas", "NumPy", "Deep Learning", "Data Visualization", "Statistics"]
    hard_skills = ["Python", "Data Analysis", "SQL"]
    soft_skills = ["Communication", "Teamwork", "Problem-solving"]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="subheader">Alignment Progress</div>', unsafe_allow_html=True)
        st.markdown('<div class="circular-progress">', unsafe_allow_html=True)
        st.plotly_chart(create_circular_progress_bar(progress), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="subheader">Top 20 Keywords in Job Description</div>', unsafe_allow_html=True)
        st.markdown('<div class="box highlight"><div class="highlight-header">Keywords</div>' + '<br>'.join(top_keywords) + '</div>', unsafe_allow_html=True)

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
