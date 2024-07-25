from src.utils import *
from src.model_setup import *



def match_score(Job_Profile,Job_Description,resume):
    response_schemas = [
        ResponseSchema(name="Match_score", description="Allignment Match Score according between Resume and Job Description")
    ]

    format_instructions = format_inst(response_schemas)
    rel_base_prompt_data_match_sc = '''
    Act as an Keyword or text Matcher of Resumes.For the {Job_Profile} position. Given the Job Description: {Job_Description} and the Resume: {resume}, perform the following tasks:
    1. Based on the text matching , skills matching and other job requirements ,calculate a match score ranging between 0-100 that tells how eligible a candidate is for the given Job.
    Make sure you only output a score.
    Provide the results in the following format: 
    {format_instructions}
    '''

    # response_schemas = [
    #     ResponseSchema(name="Output", description="Allignment Match Score details between Resume and Job Description")
    # ]

    # format_instructions = format_inst(response_schemas)
    # rel_base_prompt_data_match_sc = '''
    #         You are an intelligent system designed to assess and enhance resumes based on specific job descriptions. Your task is to calculate a score reflecting the alignment between a given resume and job description. The score should be based on the following criteria and methodology:

    #         Scoring Criteria
    #         Keyword Matching (40%)

    #         Job Title Match: Direct match of job titles.
    #         Skill Match: Presence of required skills and technologies.
    #         Experience Match: Relevant experience in years and specific job functions.
    #         Education Match: Required degrees and certifications.
    #         Content Quality (30%)

    #         Clarity and Conciseness: Clear and concise language.
    #         Grammar and Spelling: Proper grammar and spelling.
    #         Formatting: Proper use of headings, bullet points, and consistent formatting.
    #         Achievements and Impact (20%)

    #         Quantifiable Achievements: Specific metrics or outcomes (e.g., increased sales by 20%).
    #         Relevant Projects: Highlighted projects that match the job description.
    #         Additional Sections (10%)

    #         Cover Letter: Custom cover letter for the job application.
    #         Additional Certifications: Relevant certifications not explicitly required but beneficial.
    #         Professional Development: Ongoing learning and development activities.
    #         Methodology
    #         Parsing Resumes and Job Descriptions

    #         Extract relevant information from resumes and job descriptions.
    #         Identify key sections and entities (e.g., skills, experience, education).
    #         Keyword Matching

    #         Compare keywords from job descriptions with those in resumes.
    #         Assign weights to different sections based on their importance (e.g., higher weight for required skills).
    #         Content Analysis

    #         Assess the clarity, conciseness, and grammatical correctness of the resume content.
    #         Evaluate formatting consistency and readability.
    #         Achievement Analysis

    #         Identify and quantify achievements and project impacts.
    #         Compare against job description requirements and industry benchmarks.
    #         Score Calculation

    #         Aggregate scores from each criterion to generate a final alignment score.
    #         Provide a detailed breakdown of scores for each section.
    #         Optimization Suggestions

    #         Provide specific suggestions for improving the resume.
    #         Highlight areas of improvement and suggest additional skills or certifications that could enhance the resume.
    #         Input
    #         Resume: {resume}
    #         Job Description:{Job_Description}
    #         Output
    #         Alignment Score: [Provide Alignment Score Here]
    #         Detailed Breakdown of Scores:
    #         Keyword Matching: [Score]
    #         Content Quality: [Score]
    #         Achievements and Impact: [Score]
    #         Additional Sections: [Score]
    #         Optimization Suggestions:
    #         [Provide Suggestions Here]
    #         Please calculate the alignment score and provide detailed feedback based on the criteria and methodology outlined above and  Provide the results in the following format:  {format_instructions}
    # '''



    prompt = PromptTemplate(
        template = rel_base_prompt_data_match_sc,
        input_variables=["Job_Profile","Job_Description","resume"],
        partial_variables={"format_instructions": format_instructions}
    )

    _input = prompt.format_prompt(Job_Profile = Job_Profile,Job_Description = Job_Description, resume = resume)
    output = llm_chatopenai(_input.to_messages())
    # print(output)
    match_score = output_formatter(output)
    return(match_score)