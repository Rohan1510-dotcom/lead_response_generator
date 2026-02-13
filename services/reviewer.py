from services.ollama_client import call_ollama

def review_response(original_message: str, draft_reply: str):

    messages = [
        {
            "role": "system",
            "content": "Check if reply contains assumptions or guarantees. Respond SAFE or UNSAFE only."
        },
        {
            "role": "user",
            "content": f"Original: {original_message}\nReply: {draft_reply}"
        }
    ]

    return call_ollama(messages, temperature=0).strip()
