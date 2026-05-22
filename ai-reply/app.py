import json
from scorer import score_message
from openai import OpenAI
from prompts import SYSTEM_PROMPT

client = OpenAI(api_key="YOUR_API_KEY")

with open("sample_chat.json") as f:
    chats = json.load(f)

# score messages
for chat in chats:
    chat["score"] = score_message(chat)

# sort
top_messages = sorted(chats, key=lambda x: x["score"], reverse=True)[:3]

# generate replies
for msg in top_messages:

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
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