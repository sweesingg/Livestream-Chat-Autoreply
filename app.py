import json
from scorer import score_message
from openai import OpenAI
from prompts import SYSTEM_PROMPT
from dotenv import load_dotenv
import os

load_dotenv()

#print(os.getenv("OPENAI_API_KEY"))  # Check if the API key is loaded correctly

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#models = client.models.list()

#for model in models.data:
#   print(model.id)

with open("sample_chat.json", "r", encoding="utf-8") as f:
    chats = json.load(f)

# score messages
for chat in chats:
    chat["score"] = score_message(chat)
    

# sort
top_messages = sorted(chats, key=lambda x: x["score"], reverse=True)[:3]

# show top messages
print("\n=== TOP 3 PRIORITY MESSAGES ===")

for index, msg in enumerate(top_messages, start=1):

    print(f"\n#{index}")
    print(f"USER: {msg['user']}")
    print(f"MESSAGE: {msg['message']}")
    print(f"SCORE: {msg['score']}")

print("\n=== GENERATING AI REPLIES ===")

# generate replies
for msg in top_messages:

    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": msg["message"]}
        ]
    )

    reply = response.choices[0].message.content

    print("\n----------------")
    print("USER:", msg["user"])
    print("MESSAGE:", msg["message"])
    print("SCORE:", msg["score"])
    print("AI REPLY:", reply)