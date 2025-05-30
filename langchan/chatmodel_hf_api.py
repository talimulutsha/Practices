from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",  # Note: Using the non-GGUF version
    task="text-generation", 
    max_new_tokens=100
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of bd?")
print(result.content)