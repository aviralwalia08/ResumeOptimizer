# results_page.py

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from src.topKeywords_resume import *
from src.topKeywords_JD import *
from src.hardSoftSkills_JD import *
from src.hardSoftSkills_resume import *
from src.match_score import *
from src.keywords_found import *
from src.keywords_missing import *

industry = 'Data Science'
Job_Profile = 'Data Scientist'

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


# keywords_resume = top_keywords_resume(industry,Job_Profile,resume_marketing)
# print(keywords_resume[0]['TopKeywords'])





# hss_res = hardsoftSkill_res(industry,Job_Profile,resume_marketing)
# print('pooo ---->>>' ,hss_res[0]['HardSkills'] , hss_res[0]['SoftSkills'])

# score = match_score(Job_Profile,Job_Description,resume)
# print(score[0]['Match_score'],"%" )

# score = match_score(Job_Profile,Job_Description,resume_marketing)
# print(score[0]['Match_score'],"%" )




def display_results_page(resume_text, job_desc_text):
    # print('################ testing ########################')
    # print(resume_text)
    # print('========')
    # print(job_desc_text)
    # print('################testing_close########################')
    st.markdown('<div class="header">📊 Results and Suggestions</div>', unsafe_allow_html=True)
    st.write("Here are the results based on your uploaded resume and job description.")

    # Example data - in a real application, this would be dynamically generated

    # match Score
    score = match_score(Job_Profile,job_desc_text,resume_text)
    progress = int(score[0]['Match_score'])

    # top Keywords
    keywords_JD = top_keywords_JD(industry,Job_Profile,job_desc_text)
    top_keywords = keywords_JD[0]['TopKeywords']

    # Keywords match
    key_foun =  keywords_found(Job_Profile,job_desc_text,resume_text)
    keywords_matched = key_foun[0]['Keywords_Found']

    # Keywords missing
    key_mis =  keywords_missing(Job_Profile,job_desc_text,resume_text)
    keyword_missing = key_mis[0]['Keywords_Missing']

    # hard _soft_skill
    hss_JD = hardsoftSkill_JD(industry,Job_Profile,job_desc_text)
    hard_skills = hss_JD[0]['HardSkills']
    soft_skills = hss_JD[0]['SoftSkills']

    # resume_list = [f'{resume_text}']
    # jd_list = [f'{job_desc_text}']
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="subheader">Alignment Progress</div>', unsafe_allow_html=True)
        st.markdown('<div class="circular-progress">', unsafe_allow_html=True)
        st.plotly_chart(create_circular_progress_bar(progress), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="subheader">Top 20 Keywords in Job Description</div>', unsafe_allow_html=True)
        st.markdown('<div class="box highlight">' + '<br>'.join(top_keywords) + '</div>', unsafe_allow_html=True)

        st.markdown('<div class="subheader">Keywords Found in Resume</div>', unsafe_allow_html=True)
        st.markdown('<div class="box highlight">' + '<br>'.join(keywords_matched) + '</div>', unsafe_allow_html=True)

        # remove later
        # st.markdown('<div class="subheader">Resume_text</div>', unsafe_allow_html=True)
        # st.markdown('<div class="box highlight"><div class="highlight-header">Resume Text</div>' + '<br>'.join(resume_list) + '</div>', unsafe_allow_html=True)

        # st.markdown('<div class="subheader">JD_text</div>', unsafe_allow_html=True)
        # st.markdown('<div class="box highlight"><div class="highlight-header">JD Text</div>' + '<br>'.join(jd_list) + '</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="subheader">Keywords Missing in Resume</div>', unsafe_allow_html=True)
        st.markdown('<div class="box highlight">' + '<br>'.join(keyword_missing) + '</div>', unsafe_allow_html=True)

        st.markdown('<div class="subheader">Hard Skills Required</div>', unsafe_allow_html=True)
        st.markdown('<div class="box highlight">' + '<br>'.join(hard_skills) + '</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="subheader">Soft Skills Required</div>', unsafe_allow_html=True)
        st.markdown('<div class="box highlight">' + '<br>'.join(soft_skills) + '</div>', unsafe_allow_html=True)

        if st.button("Optimize"):
            # print('################res########################')
            # print(resume_text)
            # print('========')
            # print(job_desc_text)
            # print('################res_close########################')
            st.experimental_set_query_params(page="optimize_results", resume_text=resume_text, job_desc_text=job_desc_text)
            st.experimental_rerun()

    if st.button("Back", key="back"):
        st.experimental_set_query_params(page="")
        st.experimental_rerun()
