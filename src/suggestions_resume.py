

from src.utils import *
from src.model_setup import *



def suggestions_task(Job_Description,resume):
    response_schemas_key = [
        ResponseSchema(name="Suggestions", description="Suggestions made by LLM")
    ]

    # ResponseSchema(name="Keywords_Missing", description="Python List of keywords that are missing in the Resume and are also there in Job Description")

    format_instructions_key = format_inst(response_schemas_key)
    rel_base_prompt_data__key = '''Act Like a skilled or very experience ATS(Application Tracking System)
    with a deep understanding of tech field,software engineering,data science ,data analyst
    and big data engineer. Your task is to evaluate the resume based on the given job description.
    You must consider the job market is very competitive and you should provide 
    best assistance or suggestions for improving the resumes.PLease provide the suggestions in bullet points
    resume:{resume}
    description:{Job_Description}

    Provide the results in the following format: 
    {format_instructions}
    '''

    prompt = PromptTemplate(
        template = rel_base_prompt_data__key,
        input_variables=["Job_Description","resume"],
        partial_variables={"format_instructions": format_instructions_key}
    )

    _input = prompt.format_prompt(Job_Description = Job_Description, resume = resume)
    output = llm_chatopenai(_input.to_messages())
    # print('testing 1',output)
    suggestion = output_formatter(output)
    return(suggestion)