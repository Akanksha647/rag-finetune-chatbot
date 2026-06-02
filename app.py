import streamlit as st
from rag_chat import ask_question

st.set_page_config(page_title="RAG Fine-Tuning Chatbot")

st.title("Local RAG Chatbot")

question = st.text_input("Ask a question from your documents:")

if st.button("Ask"):
    if question.strip():
        answer = ask_question(question)
        st.write(answer)
    else:
        st.warning("Please enter a question.")