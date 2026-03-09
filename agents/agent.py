from langchain.agents import initialize_agent, AgentType
from llm.load_model import load_llm
from agents.tools import get_tools

def create_agent():
    llm = load_llm()
    tools = get_tools(llm)

    agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
    )
    return agent
