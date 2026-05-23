import json
from scorer import score_message
from openai import OpenAI
from prompts import SYSTEM_PROMPT
from dotenv import load_dotenv
import os
import time

# Start Timer
start_time = time.time()
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
    score, reasons = score_message(chat)
    chat["score"] = score
    chat["reasons"] = reasons

# sort
top_messages = sorted(chats, key=lambda x: x["score"], reverse=True)[:3]

# show top messages
print("\n=== TOP 3 PRIORITY MESSAGES ===")

for index, msg in enumerate(top_messages, start=1):

    print(f"\n#{index}")
    print(f"USER: {msg['user']}")
    print(f"MESSAGE: {msg['message']}")
    print(f"SCORE: {msg['score']}")
    print(f"REASONS: {', '.join(msg['reasons'])}")

print("\n=== GENERATING AI REPLIES ===")
# Building all 3 messages for batched prompt
messages_text = ""
for index, msg in enumerate(top_messages, start=1):

    messages_text += f"""
Message {index}
User: {msg['user']}
Message: {msg['message']}
"""
# Single API Call
response = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": f"""
Generate a short livestream-style reply for each message.

Rules:
- Keep replies short
- Casual Indonesian-English mix
- Sound human and spontaneous
- No long explanations

Reply ONLY in this format:

reply one || reply two || reply three

Messages:
{messages_text}
"""
        }
    ],
    max_completion_tokens=100,
    temperature=1.1
)
# get batched replies
reply_text = response.choices[0].message.content

# split replies into lines
reply_lines = [
    reply.strip()
    for reply in reply_text.split("||")
]

# print results
for index, msg in enumerate(top_messages):

    auto_reply = reply_lines[index] if index < len(reply_lines) else "No reply generated"

    print("\n----------------")
    print("USER:", msg["user"])
    print("MESSAGE:", msg["message"])
    print("SCORE:", msg["score"])
    print("AUTO REPLY:", auto_reply)

# End Timer
end_time = time.time()
duration = end_time - start_time

# Statistics
print(f"\nMessages Processed: {len(chats)}")
print(f"Messages Sent to LLM: {len(top_messages)}")
print(f"Filtered Messages: {len(chats) - len(top_messages)}")
print(f"\nTotal Processing Time: {duration:.2f} seconds")