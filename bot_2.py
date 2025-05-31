import groq as Groq
import os
from dotenv import load_dotenv
# --- Configuration (same as above) ---
load_dotenv()
GROQ_API_KEY=os.environ.get("API_KEY")
import requests
messages = []
def get_groq_response(messages):
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
},
        json={
        "model": "llama-3.3-70b-versatile",
        "messages": messages,
        "temperature": 0.7
    }
    )

    data = response.json()
    return data["choices"][0]["message"]["content"]

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        break

    #update msg history
    messages.append({"role": "user", "content": user_input})

    #output
    assistant_reply = get_groq_response(messages)
    print("AI:", assistant_reply)

    #update msg history
    messages.append({"role": "assistant", "content": assistant_reply})
