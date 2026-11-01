from typing import TypedDict

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini")


class State(TypedDict):
    question: str
    answer: str


def chatbot(state: State) -> dict:
    """One graph step: send the question to OpenAI and save the reply."""
    response = llm.invoke(state["question"])
    return {"answer": response.content}


graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()
