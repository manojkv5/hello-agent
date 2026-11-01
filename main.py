from dotenv import load_dotenv

load_dotenv()

from agent import graph

result = graph.invoke(
    {"question": "What is LangChain? Explain it in one short paragraph."}
)

print(result["answer"])
print(result["question"])
