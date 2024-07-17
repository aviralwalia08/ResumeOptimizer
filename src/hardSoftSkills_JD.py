from utils import *
from model_setup import *

response_schemas_hss = [
    ResponseSchema(name="HardSills", description="List of Hard Skill's keywords that are there in the Job Description"),
    ResponseSchema(name="SoftSkills", description="List of Soft Skill's keywords that are there in the Job Description")
]

format_instructions_hss = format_inst(response_schemas_hss)

def hardsoftSkill_JD(format_instructions, industry,Job_Profile,Job_Description):
    rel_base_prompt_data_2 = '''Act as a {industry} industry Hiring manager.For a {Job_Profile} Job Profile, Given is the Job Description {Job_Description}.Extract the list of all hard skills and soft skills keywords from the given Job Description that should be in the cadidates resume to get shortlisted for the Job .\n{format_instructions}.\n'''

    prompt = PromptTemplate(
        template = rel_base_prompt_data_2,
        input_variables=["industry" ,"Job_Profile","Job_Description"],
        partial_variables={"format_instructions": format_instructions}
    )

    _input = prompt.format_prompt(industry=industry,Job_Profile = Job_Profile,Job_Description = Job_Description)
    output = llm_chatopenai(_input.to_messages())
    hss_JD = output_formatter(output)
    return(hss_JD)
