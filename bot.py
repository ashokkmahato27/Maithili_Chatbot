import requests
import streamlit as st

st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")

def get_groq_response(text):
    response = requests.post(
        "http://127.0.0.1:8000/chain/invoke",
        json={
            "input": {
                "language": "maithili",
                "text": text
            }
        }
    )
    return response.json().get("output", "No response")

st.title("🤖 Groq Maithili Chatbot")
st.caption("समस्या के सामाधान मैथिली मे ")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("अपन प्रश्न लिखू...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("सोचैत अछि..."):
            reply = get_groq_response(user_input)
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
