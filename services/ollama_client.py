import requests

OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3"

def call_ollama(messages, temperature=0.4):

    response = requests.post(
        OLLAMA_CHAT_URL,
        json={
            "model": MODEL_NAME,
            "messages": messages,
            "stream": False,
            "options": {
                "temperature": temperature
            }
        }
    )

    data = response.json()

    # Debug safety check
    if "message" not in data:
        print("Ollama Error Response:", data)
        raise Exception("Ollama did not return expected chat format")

    return data["message"]["content"]
