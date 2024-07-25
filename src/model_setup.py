from langchain_openai import AzureChatOpenAI

llm_chatopenai = AzureChatOpenAI(
    api_key = 'put your key here',
    api_version = '2023-03-15-preview',
    azure_endpoint = 'put yours here',
    temperature = 0,
    deployment_name = 'model'
    )
