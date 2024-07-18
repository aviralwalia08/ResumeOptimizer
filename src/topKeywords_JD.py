from src.utils import *
from src.model_setup import *



def top_keywords_JD(industry,Job_Profile,Job_Description):
    response_schemas = [
    ResponseSchema(name="TopKeywords", description="List of Top 20 keywords that are there in the Job Description")
    ]

    format_instructions = format_inst(response_schemas)
    rel_base_prompt_data = '''Act as a {industry} industry Hiring manager.For a {Job_Profile} Job Profile, Given is the Job Description {Job_Description}.Extract the List of Top 20 Keywords from the given Job Description that should be in the cadidates resume to get shortlisted for the Job .\n{format_instructions}.\n'''

    prompt = PromptTemplate(
        template = rel_base_prompt_data,
        input_variables=["industry" ,"Job_Profile","Job_Description"],
        partial_variables={"format_instructions": format_instructions}
    )

    _input = prompt.format_prompt(industry=industry,Job_Profile = Job_Profile,Job_Description = Job_Description)
    output = llm_chatopenai(_input.to_messages())
    keywords_JD = output_formatter(output)
    return(keywords_JD)
