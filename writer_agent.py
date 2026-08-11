from pydantic import BaseModel, Field
from agents import Agent,OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)

openrouter_api_key = os.getenv('OPENROUTER_API_KEY')
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
openrouter_client = AsyncOpenAI(base_url=OPENROUTER_BASE_URL, api_key=openrouter_api_key)
deepseek_model = OpenAIChatCompletionsModel(model="deepseek/deepseek-v4-flash", openai_client=openrouter_client)

INSTRUCTIONS = """
You are an AI research assistant tasked with writing a cohesive, comprehensive report for a research query.
You will be provided with the original query and web research summaries.
Generate an extensive, highly detailed, and well-structured report based on the research and the query in markdown format.

IMPORTANT FORMATTING RULES:
- Start directly with the report title or Executive Summary.
- DO NOT write dates ("Current Date:", etc.), "Prepared by:", human job titles, or fake credentials anywhere in the report.
"""


class ReportData(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")
    markdown_report: str = Field(description="The final report")
    follow_up_questions: list[str] = Field(description="Suggested topics to research further")


writer_agent = Agent(name="Writer Agent", instructions=INSTRUCTIONS, model=deepseek_model, output_type=ReportData)
