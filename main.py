from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.3)

#streamlit page setup

st.set_page_config(
    page_title=" chatbot",
    page_icon = "📣",
    layout = "centered"
)

st.title(" 💬 Gen aii chatbot")


#initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


#show chat history
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg['content'])

#input box
user_prompt = st.chat_input("ask ur question ....")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user","content":user_prompt})

    response = model.invoke(
        input = [{"role":"system","content":"You are a helpful assistant"}, *st.session_state.chat_history]
    )

    assistant_response = response.content
    st.session_state.chat_history.append({"role":"assistant" , "content" : assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)


#  user query --> 
#  display user query -->
#  save query to chat_history -->
#  send the chat_history to llm -->
#  get response from llm -->
#  save response in chat_history -->
#  display response