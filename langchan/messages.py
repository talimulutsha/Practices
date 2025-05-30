from langchain_core import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
model=ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of France?"),
]
response=model.invoke(messages)
messages.append(AIMessage(content=response.content))
print(messages)
