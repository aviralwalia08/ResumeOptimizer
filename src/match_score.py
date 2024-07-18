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

    prompt = PromptTemplate(
        template = rel_base_prompt_data_match_sc,
        input_variables=["Job_Profile","Job_Description","resume"],
        partial_variables={"format_instructions": format_instructions}
    )

    _input = prompt.format_prompt(Job_Profile = Job_Profile,Job_Description = Job_Description, resume = resume)
    output = llm_chatopenai(_input.to_messages())
    match_score = output_formatter(output)
    return(match_score)