from agents import Agent, OpenAIChatCompletionsModel, function_tool
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI
from pydantic import BaseModel, Field
from tavily import TavilyClient

load_dotenv(override=True)
openrouter_api_key = os.getenv('OPENROUTER_API_KEY')
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
openrouter_client = AsyncOpenAI(base_url=OPENROUTER_BASE_URL, api_key=openrouter_api_key)
deepseek_model = OpenAIChatCompletionsModel(model="deepseek/deepseek-v4-flash", openai_client=openrouter_client)

tavily_api_key = os.getenv('TVLY_API_KEY')
tavily_client = TavilyClient(tavily_api_key)

@function_tool
def search_tool(query: str) -> str:
    """
    Performs web search using Tavily.

    :param query: The search query.
    """
    response = tavily_client.search(
        query=query,
        search_depth="advanced",
        topic="general"
    )
    results = response.get("results", [])
    formatted_results = []
    for r in results:
        title = r.get("title", "")
        url = r.get("url", "")
        content = r.get("content", "")
        formatted_results.append(f"Title: {title}\nURL: {url}\nContent: {content}")

    return "\n\n".join(formatted_results) if formatted_results else "No search results found."


INSTRUCTIONS = """
You are a research clarification agent.

Analyze the user's research query and decide whether important technical scope or domain information is missing or ambiguous before deep research begins.

CRITICAL TIMEFRAME & REAL-WORLD RULES:
- Assume the current time is 2026.
- DO NOT question, challenge, or ask about years, dates, or timeframes mentioned in the user's query (e.g. 2024, 2025, 2026, 2027+).
- NEVER ask if the query refers to a future date, training cutoff, simulation, video game, or fiction simply because a year like 2026 is mentioned.
- Treat queries about 2026 or any recent/future year as completely valid, real-world research topics.

GENERAL CLARIFICATION RULES:
- Only ask a question if its answer would materially change the technical scope, specific domain, or evaluation criteria of the research.
- If the query is sufficiently clear, set needs_clarification to False and return an empty questions list.
- Ask no more than 3 questions, and ask fewer when appropriate.
- Do not ask about information already provided.
- Do not research or answer the query itself.
"""

class ClarificationResult(BaseModel):
    needs_clarification: bool = Field(
        description="Whether the user's research query requires additional clarification before research begins."
    )

    questions: list[str] = Field(
        description="A list of concise follow-up questions that would help clarify the user's research requirements."
    )


clarification_agent = Agent(
    name="Clarification Agent",
    instructions=INSTRUCTIONS,
    model=deepseek_model,
    tools=[search_tool],
    output_type=ClarificationResult
)