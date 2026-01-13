import os
from dotenv import load_dotenv
import streamlit as st
import requests
import json
import time

load_dotenv()

st.set_page_config(page_title="AI Chatbot Sederhana", page_icon="🤖")

# Kustomisasi CSS untuk tema gelap
st.markdown("""
<style>
/* Background utama */
.stApp {
    background-color: #0f172a;
    color: #e5e7eb;
}

/* Header */
h1 {
    color: #38bdf8;
    text-align: center;
}

/* Chat bubble user */
[data-testid="chat-message-user"] {
    background-color: #1e293b;
    border-radius: 12px;
    padding: 10px;
    color: #e5e7eb;
}

/* Chat bubble assistant */
[data-testid="chat-message-assistant"] {
    background-color: #020617;
    border-radius: 12px;
    padding: 10px;
    border-left: 4px solid #38bdf8;
    color: #e5e7eb;
}

/* Paksa warna teks di dalam chat */
[data-testid="chat-message-user"] * ,
[data-testid="chat-message-assistant"] * {
    color: #e5e7eb !important;
}

/* Input chat */
textarea {
    background-color: #020617 !important;
    color: #e5e7eb !important;
    border-radius: 8px !important;
}

/* Button */
button {
    background-color: #38bdf8 !important;
    color: black !important;
    border-radius: 8px !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Judul Aplikasi
st.title("🤖 AI Chatbot Sederhana")
st.caption("Powered by OpenRouter • Streamlit")

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "mistralai/mistral-7b-instruct:free"

if not API_KEY:
    st.error("API Key belum di-set. Silakan set OPENROUTER_API_KEY.")
    st.stop()

def clean_response(text):
    for token in ["<s>", "</s>", "<assistant>", "</assistant>", "[OUT]", "[/OUT]"]:
        text = text.replace(token, "")
    return text.strip()


def get_ai_response(messages, max_retries=3, delay=2):
    for attempt in range(max_retries):
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": MODEL,
                    "messages": messages
                },
                timeout=30
            )

            data = response.json()

            # Jika API sukses
            if "choices" in data:
                raw = data["choices"][0]["message"]["content"]
                return clean_response(raw)

            # Jika API error (rate limit atau lainnya)
            error_msg = data.get("error", {}).get("message", "API error")
            time.sleep(delay)

        except Exception:
            time.sleep(delay)

    # Kalau semua retry gagal
    return "⚠️ AI sedang sibuk. Coba lagi sebentar."


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
    st.rerun()
