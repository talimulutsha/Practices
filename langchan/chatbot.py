from langchain_openai import ChatOpenAI
from langchain_core import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()
model=ChatOpenAI()


Chat_history = [
    SystemMessage(content="You are a helpful assistant.")


]

while True:
    user_input= input("User: ")
    Chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    response=model.invoke(Chat_history)
    Chat_history.append(AIMessage(content=response.content)) 
    print("Bot: ", response)

print("Chat history:")