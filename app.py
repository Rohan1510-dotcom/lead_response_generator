import streamlit as st
import requests
import json

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3"


def call_ollama(messages, temperature=0.4):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "messages": messages,
            "stream": False,
            "options": {"temperature": temperature}
        }
    )

    data = response.json()
    return data.get("message", {}).get("content", "Error from Ollama")


def detect_intent(message):
    messages = [
        {
            "role": "system",
            "content": "Classify intent into: Complaint, Technical Issue, Service Request, General Inquiry, Emergency. Return only the label."
        },
        {"role": "user", "content": message}
    ]

    return call_ollama(messages, temperature=0).strip()


def extract_information(message):
    messages = [
        {
            "role": "system",
            "content": """
Extract structured information.

Return ONLY valid JSON:

{
  "issue_type": "",
  "location": "",
  "trigger": "",
  "urgency": "low/medium/high"
}
Do not add explanation.
"""
        },
        {"role": "user", "content": message}
    ]

    response = call_ollama(messages, temperature=0)

    try:
        return json.loads(response)
    except:
        return {
            "issue_type": None,
            "location": None,
            "trigger": None,
            "urgency": "medium"
        }


def generate_response(user_message):

    # Add user message to history
    st.session_state.chat_history.append(
        {"role": "user", "content": user_message}
    )

    # Prepare full conversation
    messages = [
        {
            "role": "system",
            "content": """
You are a professional customer support assistant.

- Acknowledge the concern
- Ask relevant follow-up questions
- Provide safe next steps
- Do NOT assume facts
- Do NOT promise guarantees
- Sound natural
"""
        }
    ] + st.session_state.chat_history

    reply = call_ollama(messages, temperature=0.6)

    # Add assistant reply to history
    st.session_state.chat_history.append(
        {"role": "assistant", "content": reply}
    )

    return reply



# ---------------- STREAMLIT UI ----------------

st.title("🧠 Lead Response Assistant")

user_input = st.text_input("You:")

if st.button("Send"):

    if user_input.strip() != "":
        reply = generate_response(user_input)

# Display conversation
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"**You:** {chat['content']}")
    else:
        st.markdown(f"**Assistant:** {chat['content']}")

if st.button("Reset Conversation"):
    st.session_state.chat_history = []


