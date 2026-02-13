from services.ollama_client import call_ollama

def generate_response(message: str):

    messages = [
        {
            "role": "system",
            "content": """
You are a professional customer support assistant.

When responding:
- Acknowledge the concern empathetically.
- Ask at least 2 relevant follow-up questions.
- Provide safe next steps.
- Do not assume facts not mentioned.
- Do not guarantee results.
- Sound natural and human.
"""
        },
        {
            "role": "user",
            "content": message
        }
    ]

    return call_ollama(messages, temperature=0.6)
