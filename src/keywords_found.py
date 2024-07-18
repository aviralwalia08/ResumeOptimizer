from src.utils import *
from src.model_setup import *



def keywords_found(Job_Profile,Job_Description,resume):
    response_schemas_key = [
        ResponseSchema(name="Keywords_Found", description="Python List of keywords that are found in the Resume and are also there in Job Description")
    ]

    # ResponseSchema(name="Keywords_Missing", description="Python List of keywords that are missing in the Resume and are also there in Job Description")

    format_instructions_key = format_inst(response_schemas_key)
    rel_base_prompt_data__key = '''
    Act as a Keyword or Text Matcher of Resumes. For the {Job_Profile} position, given the Job Description: {Job_Description} and the Resume: {resume}, perform the following tasks:
    1. Extract and list all keywords that are in the resume which match the keywords found in the given job description.
    Make sure you provide the results in the following format: 
    {format_instructions}
    '''

    prompt = PromptTemplate(
        template = rel_base_prompt_data__key,
        input_variables=["Job_Profile","Job_Description","resume"],
        partial_variables={"format_instructions": format_instructions_key}
    )

    _input = prompt.format_prompt(Job_Profile = Job_Profile,Job_Description = Job_Description, resume = resume)
    output = llm_chatopenai(_input.to_messages())
    key_foun = output_formatter(output)
    return(key_foun)