from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import OpenAI
from langchain_tavily import TavilySearch

load_dotenv()  # Load environment variables from .env file

@tool
def triple(num: float) -> float:
    """
    param num: A number to be tripled.
    return: The tripled value of the input number.
    """
    return float(num) * 3

tools = [TavilySearch(max_results=1), triple]

llm = OpenAI(model="gpt-4o-mini", temperature=0).bind_tools(tools)



