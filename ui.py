import streamlit as st
from db import get_history, create_message

st.set_page_config(page_title="ChatBot", layout= "centered")

st.title("Chatbot")
st.caption("Find train tickets, delays - all through chat")

if "message" not in st.session_state:
    st.session_state.chat = get_history()

for message in st.session_state.chat:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

user_input = st.chat_input("You: ")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat.append({"role": "user", "text": user_input})
    create_message("user", user_input)

    if user_input.lower() in ["exit", "quit", "bye"]:
        response = "Chatbot: Goodbye!"
    else:
        response = f"Chatbot: You said '{user_input}'"

    st.chat_message("assistant").markdown(response)
    st.session_state.chat.append({"role": "assistant", "text": response})
    create_message("assistant", response)