from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the DeepSeek API key
api_key = os.getenv("DEEPSEEK_API_KEY")

# Validate that the API key was loaded
if not api_key:
    raise ValueError("❌ DEEPSEEK_API_KEY not found. Please check your .env file.")

# Define the DeepSeek R1-compatible base URL
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"

# Initialize the LangChain LLM client for DeepSeek R1
llm = ChatOpenAI(
    model="deepseek-chat",
    openai_api_key=api_key,
    openai_api_base=DEEPSEEK_BASE_URL,
    temperature=0.7
)

# Prompt the model
response = llm.invoke("What is the capital of France?")
print("🧠 DeepSeek R1 Response:", response)
