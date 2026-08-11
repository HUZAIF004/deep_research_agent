from agents import Agent, OpenAIChatCompletionsModel, function_tool,ModelSettings
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI
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
You are a research assistant. Given a search term, you MUST use the search_tool to search the web for that term first, then produce a concise summary of the results. The summary must be 2-3 paragraphs and less than 300 words.
Capture the main points and be succinct. Reply only with the summary.
"""

tools = [search_tool]
settings = ModelSettings(tool_choice="required")

search_agent = Agent(
    name="Search Agent",
    instructions=INSTRUCTIONS,
    tools=tools,
    model_settings=settings,
    model=deepseek_model
)