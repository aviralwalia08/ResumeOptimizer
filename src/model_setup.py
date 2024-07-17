from langchain_openai import AzureChatOpenAI

llm_chatopenai = AzureChatOpenAI(
    api_key = 'ab40db4c57884de3bf7d8517677ab90e',
    api_version = '2023-03-15-preview',
    azure_endpoint = 'https://lucidmvpopenai.openai.azure.com/',
    temperature = 0,
    deployment_name = 'lucidpg'
    )