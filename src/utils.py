import PyPDF2
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from datetime import datetime
import numpy as np
import re
import pandas as pd
import os
import json
import pandas as pd
from datetime import datetime
import os
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
import json_repair

def input_pdf_text(uploaded_file):
    reader=PyPDF2.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

def output_formatter(output:str):
    extracted_json = re.search(r'```json\n([\s\S]*?)\n```', output.content)
    if extracted_json:
        json_string = extracted_json.group(1)
    else:
        json_string = "[]"  # Fallback to an empty JSON array in case the extraction fails

    # Now, parse the extracted JSON string
    data = json_repair.loads(f"[{json_string}]")
    return(data)

def format_inst(response_schemas):
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()
    return format_instructions