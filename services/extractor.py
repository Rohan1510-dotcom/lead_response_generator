import json
from services.ollama_client import call_ollama

def extract_information(message: str):

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
        {
            "role": "user",
            "content": message
        }
    ]

    response = call_ollama(messages, temperature=0)

    try:
        return json.loads(response)
    except:
        print("JSON Parse Error:", response)
        return {
            "issue_type": None,
            "location": None,
            "trigger": None,
            "urgency": "medium"
        }
