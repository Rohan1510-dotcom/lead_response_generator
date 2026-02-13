from services.ollama_client import call_ollama

def detect_intent(message: str):

    messages = [
        {
            "role": "system",
            "content": "Classify the intent into: Complaint, Technical Issue, Service Request, General Inquiry, Emergency. Return only the label."
        },
        {
            "role": "user",
            "content": message
        }
    ]

    return call_ollama(messages, temperature=0).strip()
