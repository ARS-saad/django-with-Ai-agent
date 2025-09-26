from langgraph.prebuilt import create_react_agent
# from langchain.agents import initialize_agent, AgentType
from ai.llms import get_openai_model
from ai.tools import document_tools

def get_agent():
    model = get_openai_model()

    if model is None:
            raise ValueError("Could not initialize the OpenAI model. API key may be missing.")

    agent = create_react_agent(
        model=model,
        tools=document_tools,
        prompt="You are a helpful assistant in managing a user's documents within this app",
    )
    return agent
