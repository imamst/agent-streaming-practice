import os
from agents import function_tool
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

tavily_client = TavilyClient(os.getenv("TAVILY_API_KEY"))


@function_tool
def search_web(query: str):
    results = tavily_client.search(query, max_results=1)

    return results
