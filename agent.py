from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os
import warnings
import json

warnings.filterwarnings('ignore')
load_dotenv()


class StructuredResponse(BaseModel):
    has_dementia: bool
    diagnosis_reason: str
    dementia_severity: str | None
    prevention_or_treatment: str
    markdown_input_table: str
    markdown_score_table: str
    short_summary: str
    full_markdown_report: str

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

Model = ChatGroq(
    api_key=GROQ_API_KEY,
    temperature=0,
    model="openai/gpt-oss-20b"
)

Dimentia_Model = Model.with_structured_output(schema=StructuredResponse)


prompt_for_llm = PromptTemplate(
    input_variables=[
        "Gender", "Age", "EDUC", "MMSE", "CDR", "eTIV", "nWBV", "ASF"
    ],
    template="""
You are an expert clinical LLM specializing in early dementia detection using MRI metadata and cognitive scores.

Analyze the patient information and produce a structured response following the JSON schema.

# Patient Data
- Gender: {Gender}
- Age: {Age}
- Education: {EDUC}
- MMSE: {MMSE}
- CDR: {CDR}
- eTIV: {eTIV}
- nWBV: {nWBV}
- ASF: {ASF}

Generate only the structured fields. No additional explanations.
"""
)

def analyze_dementia(patient_data: dict) -> StructuredResponse:
    chain = prompt_for_llm | Dimentia_Model
    result = chain.invoke(patient_data)
    return result


if __name__ == "__main__":
    result = analyze_dementia({
        "Gender": "M",
        "Age": "72",
        "EDUC": "16",
        "MMSE": "28",
        "CDR": "0",
        "eTIV": "1500",
        "nWBV": "0.72",
        "ASF": "1.12"
    })
    print(result)