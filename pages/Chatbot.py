import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize session states
if "messages" not in st.session_state:
    st.session_state.messages = []

if "conversation" not in st.session_state:
    memory = ConversationBufferMemory()
    llm = ChatGroq(model_name="llama3-8b-8192", groq_api_key=groq_api_key)
    
    prompt_template = PromptTemplate(
        input_variables=["history", "input"],
        template="""
        You are an AI-powered healthcare assistant.
        Your goal is to engage with patients and provide preliminary symptom assessment.
        You can ask follow-up questions to better understand their condition and suggest whether they should consult a doctor.
        
        Previous conversation:
        {history}
        
        Patient: {input}
        AI:
        """
    )
    
    st.session_state.conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True,
        prompt=prompt_template
    )

# Page title and description
st.title("🩺 AI Healthcare Assistant")
st.write("Chat with an AI-powered assistant for preliminary symptom assessment and guidance.")

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Describe your symptoms..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.conversation.predict(input=prompt)
            st.markdown(response)
            
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Disclaimer
st.markdown("---")
st.markdown("⚠ *Disclaimer*: This AI is for informational purposes only and does not provide medical diagnoses. Please consult a doctor for professional medical advice.")

# Add a clear chat button
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.session_state.conversation.memory.clear()
    st.experimental_rerun()
