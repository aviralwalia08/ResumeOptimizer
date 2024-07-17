response_schemas = [
    ResponseSchema(name="Keywords_Found", description="List of keywords that are found in the Resume and are also there in Job Description"),
    ResponseSchema(name="Keywords_Missing", description="List of keywords that are missing in the Resume and are also there in Job Description")
]
rel_base_prompt_data_2 = '''
Act as an Keyword or text Matcher of Resumes.For the {Job_Profile} position. Given the Job Description: {Job_Description} and the Resume: {resume}, perform the following tasks:
1. Extract and list all keywords found in both the resume and the job description.
2. Extract and list all keywords present in the job description but missing from the resume.
Make sure you only output both the lists and nothing else in pre or post and the keywords found should be from Resume and Keywords missing should be from Job Description only.
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
key_mis_foun = output_formatter(output)
print(key_mis_foun)