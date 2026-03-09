from langchain_community.tools import Tool

from rag.retrieve import retrieve_logs
from agents.prompts import ANALYSIS_PROMPT, RECOMMEND_PROMPT

def fetch_logs_tool(query):
    return retrieve_logs(query)

def analyze_tool(logs, llm):
    prompt = ANALYSIS_PROMPT.format(logs=logs)
    return llm(prompt)

def recommend_tool(analysis, llm):
    prompt = RECOMMEND_PROMPT.format(analysis=analysis)
    return llm(prompt)

def get_tools(llm):
    return [
        Tool(
            name="Fetch Telecom Logs",
            func=fetch_logs_tool,
            description="Fetch relevant telecom logs using semantic search"
        ),
        Tool(
            name="Analyze Call Drops",
            func=lambda x: analyze_tool(x, llm),
            description="Analyze logs to find root cause of call drops"
        ),
        Tool(
            name="Recommend Solutions",
            func=lambda x: recommend_tool(x, llm),
            description="Recommend solutions for telecom issues"
        )
    ]
