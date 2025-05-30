from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
import time

load_dotenv()

# App Setup
st.set_page_config(page_title="🤖 Research Assistant", layout="centered")
st.title("🔍 Free Research Assistant")

# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input
if prompt := st.chat_input("Ask anything..."):
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                llm = HuggingFaceEndpoint(
                    repo_id="google/flan-t5-xxl",
                    task="text-generation",
                    max_new_tokens=512
                )
                response = ChatHuggingFace(llm=llm).invoke(prompt)
                
                # Stream response
                response_text = ""
                container = st.empty()
                for chunk in response.content.split():
                    response_text += chunk + " "
                    container.write(response_text)
                    time.sleep(0.05)
                
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("This model may need GPU. Try Solution 2 from code comments.")