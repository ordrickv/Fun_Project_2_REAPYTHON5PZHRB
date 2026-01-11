import os
from dotenv import load_dotenv
import streamlit as st
import requests
import json

load_dotenv()

st.set_page_config(page_title="AI Chatbot Sederhana", page_icon="🤖")
st.title("AI Chatbot Sederhana")
st.caption("Powered by OpenRouter • Streamlit")

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "mistralai/mistral-7b-instruct:free"

if not API_KEY:
    st.error("API Key belum di-set. Silakan set OPENROUTER_API_KEY.")
    st.stop()

def get_ai_response(messages):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "messages": messages
        }
    )
    data = response.json()
    return data["choices"][0]["message"]["content"]

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Tulis pesan..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("AI sedang berpikir..."):
            reply = get_ai_response(st.session_state.messages)
            st.write(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

if st.button("Hapus Riwayat Obrolan"):
    st.session_state.messages = []
