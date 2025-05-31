from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY=os.environ.get("API_KEY")
client = Groq(api_key=GROQ_API_KEY)

messages=[]
while True:
    user_input=input("YOU:")
    if user_input.lower()=="exit":
        break
    if user_input.strip()=="":
        print("to stop type exit")
        continue
    messages.append({"role":"user", "content": user_input})
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7
    )
    print("AI:", response.choices[0].message.content)
    messages.append({"role": "assistant", "content": response.choices[0].message.content})