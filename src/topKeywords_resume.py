from utils import *
from model_setup import *

response_schemas = [
    ResponseSchema(name="TopKeywords", description="List of Top 20 keywords that are there in the Resume")
]

format_instructions = format_inst(response_schemas)


def top_keywords_resume(format_instructions, industry,Job_Profile,resume):
    rel_base_prompt_data = '''Act as a {industry} industry Hiring manager.For a {Job_Profile} Job Profile, Given is the Resume {resume}.Extract the List of Top 20 Keywords from the given Resume that are there in the cadidates resume to get shortlisted for the Job .\n{format_instructions}.\n'''

    prompt = PromptTemplate(
        template = rel_base_prompt_data,
        input_variables=["industry" ,"Job_Profile" ,"resume"],
        partial_variables={"format_instructions": format_instructions}
    )

    _input = prompt.format_prompt(industry=industry,Job_Profile = Job_Profile, resume = resume)
    output = llm_chatopenai(_input.to_messages())
    keywords_resume = output_formatter(output)
    return(keywords_resume)