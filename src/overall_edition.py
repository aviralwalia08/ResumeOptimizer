from src.utils import *
from src.model_setup import *

def overall_edit(industry,Job_Profile,Job_Description,resume):
    response_schemas_key = [
        ResponseSchema(name="Updated_Resume", description="Updated Resume according to the Job Description")
    ]

    format_instructions_key = format_inst(response_schemas_key)
    rel_base_prompt_data__key = '''
    You are an expert resume optimizer with a deep understanding of various industries and job profiles. Your task is to customize a resume to align perfectly with a given job description without adding any experiences or skills the candidate does not possess. Modify only the descriptions of the candidate's current job roles by adding or removing keywords to better match the job description, while ensuring all information remains truthful.

    Inputs:
    Industry: {industry}
    Job Profile: {Job_Profile}
    Candidate's Resume: {resume}
    Job Description: {Job_Description}

    Instructions:
    Analyze the Job Description: Identify the key skills, qualifications, and experiences required for the job profile in the specified industry.
    Review the Candidate's Resume: Carefully examine the candidate's resume to find existing job roles and experiences that can be modified to better align with the job description.
    Modify Existing Job Roles: Edit the descriptions of the candidate's current job roles by adding or removing keywords to highlight relevant experiences, skills, and accomplishments that match the job description. Ensure the modifications reflect the candidate's true qualifications.
    Ensure Accuracy and Integrity: Do not add any experiences or skills that the candidate does not possess. The resume must reflect the candidate's actual job roles and experiences.
    Optimize for Clarity and Impact: Make sure the customized resume is clear, concise, and impactful. Arrange the information in a way that makes the candidate's qualifications stand out to potential employers.
    
    Output:
    Provide a customized version of the candidate's resume that aligns with the given job description by modifying only the descriptions of the candidate's current job roles through the addition or removal of keywords, ensuring all information is accurate and truthful.
    Make sure you provide the results in the following format: 
    {format_instructions}
    '''

    prompt = PromptTemplate(
        template = rel_base_prompt_data__key,
        input_variables=["industry","Job_Profile","Job_Description","resume"],
        partial_variables={"format_instructions": format_instructions_key}
    )

    _input = prompt.format_prompt(industry = industry , Job_Profile = Job_Profile,Job_Description = Job_Description, resume = resume)
    output = llm_chatopenai(_input.to_messages())
    overal_edit = output_formatter(output)
    return(overal_edit)

# if __name__ == "__main__":

#     industry = 'Data Science'
#     Job_Profile = 'Data Scientist'
#     Job_Description = """
#     We are currently looking for a new Intermediate Data Scientist, to join our Data Insights team and work closely with Clio’s products and business teams.

#     You thrive on both analytical challenges and working closely with product development and customer-facing professionals. You will collaborate with everyone from product managers to business leaders and developers, and will guide rapid iterations of hypothesis, prioritization, experimentation / analysis and strategy setting – extract valuable insights, enhance our decision-making processes and contribute to the development of innovative financial products.

    

#     The team:
#     You will be working alongside a cross-functional team of data scientists, embedded within Clio’s products and business teams, developing AI and ML solutions to understand Clio’s customers, to bring them cutting-edge AI and GenAI products, and to recommend proactive and efficient ways to serve them better. You will play an integral role, enabling business leaders across Clio make rigorous data-driven decisions. You will help our business grow, help our customers succeed, and continuously improve the way we operate.


    

#     Who you are:
#     We aren’t looking for just any traditional Data Scientist to join this team. We’re looking for someone who takes data seriously, thrives in a rapid-growth, high-velocity environment, and lives and breathes our values. We’re looking for an innovator and a thought leader! We’re looking for someone who is:

#     Passionate about driving growth empirically;

#     Always looking to innovate with data and explore open-ended questions;

#     Strategically minded and never shies away from a challenge;

#     Self-motivated and able to work autonomously and collaboratively;

#     Agile and responsive, and comfortable with constant change.

#     You will help lay the foundation for this work by ensuring good data quality, data governance, and analytical practices. And you will also be part of our larger Data & AI team for learning, career development, and company-wide data initiatives.

#     What you'll work on:
#     Collaborate with the Clio products teams to refine business problems, develop hypotheses, and provide input that drives growth.

#     Suggest new questions about our business, product, and customers that lead to impactful insights.

#     Work with other team members to develop predictive AI and ML solutions and deploy them in production.

#     Apply rigorous statistical analysis and data mining techniques to evaluate impact of different product features and other business initiatives.

#     Employ statistical analysis, machine learning, GenAI, LLMs, etc. to unlock new product opportunities.

#     Support scientific thinking in product and business teams by enabling discussions with data, disseminating best practices, and leading by example.

#     Effectively communicate complex technical concepts and findings to both technical and non-technical audiences.

#     What you may have:
#     3+ years applied experience in data science.

#     The ability to translate business requirements into data science solutions.

#     Experience in developing analysis in Python and experience with relevant ML libraries and frameworks (e.g., pandas, PyTorch, scikit-learn)

#     Strong team player mindset, while able to work under your own initiative and prioritize time and tasks effectively.

#     Excellent written and verbal communication skills.

#     Ability to write structured SQL queries for answering questions and manipulating data.

#     Serious bonus points if you have:
#     Understanding of SaaS business metrics and growth drivers.

#     Experience with FinTech concepts.

#     Experience in analytics working with product and user behavior data, e.g., retention or churn analysis

#     Experience with building ML/AI pipelines and relevant tools (e.g., Kedro, MLFLow)

#     Experience with large data sets and user behavior data.

#     Experience with NLP and LLMs.

#     A graduate degree in a relevant quantitative discipline (computer science, statistics, mathematics, physics, engineering) 

#     What you will find here:

#     Compensation is one of the main components of Clio’s Total Rewards Program. We have developed a series of programs and processes to ensure we are creating fair and competitive pay practices that form the foundation of our human and high-performing culture.
    

#     Some highlights of our Total Rewards program include:

#     Competitive, equitable salary with top-tier health benefits, dental, and vision insurance 

#     Hybrid work environment, with expectation for local Clions (Vancouver, Calgary, Toronto, and Dublin) to be in office min. once per week on our Anchor Day. 

#     Flexible time off policy, with an encouraged 20 days off per year.

#     $2000 annual counseling benefit

#     RRSP matching and RESP contribution 

#     Clioversary recognition program with special acknowledgement at 3, 5, 7, and 10 years​

#     The expected salary range* for this role is $106,500 to $144,200 CAD. Please note there are a separate set of salary bands for other regions based on local currency.
#     *Our salary bands are designed to reflect the range of skills and experience needed for the position and to allow room for growth at Clio. For experienced individuals, we typically hire at or around the midpoint of the band. The top portion of the salary band is reserved for employees who demonstrate sustained high performance and impact at Clio. Those who are new to the role may join below the midpoint and develop their skills over time. The final offer amount for this role will be dependent on geographical region, applicable experience, and skillset of the candidate.

#     Diversity, Inclusion, Belonging and Equity (DIBE) & Accessibility 

#     Our team shows up as their authentic selves, and are united by our mission. We are dedicated to diversity, equity and inclusion. We pride ourselves in building and fostering an environment where our teams feel included, valued, and enabled to do the best work of their careers, wherever they choose to log in from. We believe that different perspectives, skills, backgrounds, and experiences result in higher-performing teams and better innovation. We are committed to equal employment and we encourage candidates from all backgrounds to apply.

#     Clio provides accessibility accommodations during the recruitment process. Should you require any accommodation, please let us know and we will work with you to meet your needs."""

#     resume = """ 
#     Aviral Walia

#     Contact Information:

#     Address: 789 Market St, Toronto, ON M3B 2S5
#     Phone: (123) 456-7890
#     Email: aviral.walia@example.com
#     LinkedIn: linkedin.com/in/aviralwalia
#     Professional Summary:
#     Insightful and analytical Market Researcher with over 4 years of experience in gathering, analyzing, and interpreting data to help companies make informed business decisions. Proficient in statistical analysis, survey design, and data visualization. Strong background in consumer behavior, market trends, and competitive analysis. Seeking to leverage my skills and expertise to drive data-driven strategies and business growth.

#     Professional Experience:

#     Market Research Analyst
#     ABC Market Solutions, Toronto, ON
#     Jan 2021 – Present

#     Conducted primary and secondary research to gather market intelligence on consumer preferences and industry trends.
#     Designed and administered surveys and questionnaires to collect quantitative and qualitative data.
#     Analyzed data using statistical software (SPSS, R) and presented findings to stakeholders through comprehensive reports and visualizations.
#     Identified market opportunities and provided actionable insights that contributed to a 15% increase in client sales.
#     Assistant Market Researcher
#     XYZ Insights, Toronto, ON
#     Jul 2018 – Dec 2020

#     Assisted in the design and execution of research projects, including data collection, analysis, and reporting.
#     Monitored and analyzed competitors' marketing strategies and performance metrics.
#     Developed and maintained databases of market research information and client contacts.
#     Supported senior researchers in preparing presentations and delivering insights to clients.
#     Education:

#     Bachelor of Science in Marketing
#     University of Toronto, Toronto, ON
#     2018

#     Skills:

#     Market Research: Survey Design, Data Collection, Competitive Analysis
#     Data Analysis: SPSS, R, Excel
#     Data Visualization: Tableau, Power BI
#     Statistical Analysis: Regression Analysis, Factor Analysis, Cluster Analysis
#     Communication: Report Writing, Presentation Skills
#     Certifications:

#     Certified Market Research Professional (CMRP)
#     Projects:

#     Consumer Behavior Study: Led a study on consumer behavior in the e-commerce sector, identifying key factors influencing purchase decisions and providing recommendations to improve customer retention.
#     Market Entry Analysis: Conducted a market entry analysis for a new product line, assessing market size, competition, and potential barriers, resulting in a successful product launch.
#     Brand Perception Survey: Designed and executed a brand perception survey for a leading retail company, analyzing customer feedback and suggesting strategies to enhance brand image."""
#     upd_res = overall_edit(industry,Job_Profile,Job_Description,resume)
#     file_path = "output3.txt"

#     # Open the file in write mode and save the string
#     with open(file_path, "w") as file:
#         file.write(upd_res[0]['Updated_Resume'])

