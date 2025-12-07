from langchain_openai import AzureChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate
from config import load_env

load_env()


def build_agent(tool):

    llm = AzureChatOpenAI(
        azure_deployment="gpt-4o",
        api_version="2025-01-01-preview",
        temperature=0
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are a research assistant. Use pdf_retrieve when factual support is needed."),
        ("human", "{input}"),
        ("assistant", "{agent_scratchpad}")
    ])

    agent = create_tool_calling_agent(llm, [tool], prompt)

    return AgentExecutor(agent=agent, tools=[tool])
