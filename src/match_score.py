response_schemas = [
    ResponseSchema(name="Match_score", description="Eligibility match score according to Resume and Job Description")
]
rel_base_prompt_data_2 = '''
Act as an Keyword or text Matcher of Resumes.For the {Job_Profile} position. Given the Job Description: {Job_Description} and the Resume: {resume}, perform the following tasks:
1. Based on the text matching , skills matching and other job requirements ,calculate a match score ranging between 0-100 that tells how eligible a candidate is for the given Job.
Make sure you only output a score.
Provide the results in the following format: 
{format_instructions}
'''

prompt = PromptTemplate(
    template = rel_base_prompt_data_2,
    input_variables=["industry" ,"Job_Profile","Job_Description","resume"],
    partial_variables={"format_instructions": format_instructions}
)

_input = prompt.format_prompt(industry=industry,Job_Profile = Job_Profile,Job_Description = Job_Description, resume = resume_marketing)
output = llm_chatopenai(_input.to_messages())
match_score = output_formatter(output)
print(match_score)