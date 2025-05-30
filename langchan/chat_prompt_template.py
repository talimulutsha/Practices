from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template= ChatPromptTemplate([
    SystemMessage(content="You are a helpful {domain}expart assistant."),
    HumanMessage(content="Explain in simple terms, what is {topic}")
])

prompt= chat_template.invoke({"domain":"python","topic":"decorators"})
print(prompt) 
