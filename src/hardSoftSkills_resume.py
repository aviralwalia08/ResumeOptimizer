response_schemas = [
    ResponseSchema(name="HardSills", description="List of Hard Skill's keywords that are there in the Job Description"),
    ResponseSchema(name="SoftSkills", description="List of Soft Skill's keywords that are there in the Job Description")
]
rel_base_prompt_data_2 = '''Act as a {industry} industry Hiring manager.For a {Job_Profile} Job Profile, Given is the Resume {resume}.Extract the list of all hard skills and soft skills keywords from the given Resume that are in the cadidates resume to get shortlisted for the Job .\n{format_instructions}.\n'''

prompt = PromptTemplate(
    template = rel_base_prompt_data_2,
    input_variables=["industry" ,"Job_Profile","Job_Description"],
    partial_variables={"format_instructions": format_instructions}
)

_input = prompt.format_prompt(industry=industry,Job_Profile = Job_Profile,resume = resume_marketing)
output = llm_chatopenai(_input.to_messages())
hss_Res = output_formatter(output)
print(hss_Res)
hss_JD[0]['HardSkills'] , hss_JD[0]['SoftSkills']