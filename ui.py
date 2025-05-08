# User interface file - Justin Picksley
# Libraries: Streamlit - Python framework for creating UI

import streamlit as st
import db
import uuid

st.set_page_config(page_title="ChatBot", layout= "centered")

st.title("Chatbot")
st.caption("Find train tickets, delays - all through chat")

def create_convo():
    new_id = str(uuid.uuid4())
    st.session_state.conversation_id = new_id
    st.session_state.chat = []
    st.sidebar.success(f"Started new chat: {new_id[:8]}")
    st.rerun()

# Creates new conversation when going on the app for the first time
if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = str (uuid.uuid4())
    st.session_state.chat = []
    
st.sidebar.header("Convos")

# Button for creating a new conversation
if st.sidebar.button("Start New Conversation"):
    create_convo()

# Button for deleting current selected conversation
if st.sidebar.button("Delete conversation"):
    db.delete_convo(st.session_state.conversation_id)
    create_convo()

convos = db.get_convos()
convos.sort()

if st.session_state.conversation_id not in convos:
    convos = [st.session_state.conversation_id] + convos

# Displaying conversations
if convos:
    selected = st.sidebar.selectbox(
        "Conversations",
        options=convos,
        index=convos.index(st.session_state.conversation_id)
        if st.session_state.conversation_id in convos else 0,
    )
    if selected != st.session_state.conversation_id:
        st.session_state.conversation_id = selected
        st.session_state.chat = db.get_history(selected)
        st.rerun()

if not st.session_state.chat:
    st.session_state.chat = db.get_history(st.session_state.conversation_id)

# Displaying messages
for message in st.session_state.chat:
    time = message.get("timestamp")
    fTime = time.strftime("%Y-%m-%d %H:%M") if time else "Unknown time"

    text = f"{message['text']}  \n*{fTime}*"
    with st.chat_message(message["role"]):
        st.markdown(text)

# Quick prompts 

column1, column2 = st.columns(2)    

prompt = None

if column1.button("Cheapest Norwich -> London"):
    prompt = "What's the cheapest ticket from Norwich to London"

if column2.button("Delay from Liverpool Street?"):
    prompt = "Is my train delayed from Liverpool Street?"

user_input = st.chat_input("You: ")

if user_input: 
    prompt = user_input

# Creating messages in database, from convo
if prompt:

    st.chat_message("user").markdown(prompt)
    st.session_state.chat.append({"role": "user", "text": prompt})
    db.create_message("user", prompt, st.session_state["conversation_id"])

    if prompt.lower() in ["exit", "quit", "bye"]:
        response = "Chatbot: Goodbye!"
    else:
        response = f"Chatbot: You said '{prompt}'"

    st.chat_message("assistant").markdown(response)
    st.session_state.chat.append({"role": "assistant", "text": response})
    db.create_message("assistant", response, st.session_state["conversation_id"])