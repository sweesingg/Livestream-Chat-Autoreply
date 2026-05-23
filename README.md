# Livestream Chat Autoreply
A lightweight AI copilot prototype that prioritizes livestream chat messages and generates human-like streamer replies in real time. <br>
<br>
The system uses rule-based filtering to shortlist high-priority messages before sending only selected chats to the LLM, reducing latency and improving scalability.

## Problem Context
Livestream chats move extremely quickly, often reaching 60–80 messages per minute.

Streamers cannot respond to every message, so the system must:
- prioritize high-value interactions,
- sound natural and human,
- avoid brute-force LLM processing on every message,
- maintain low latency for real-time interaction.

## Introduction
As a livestreamer, the following matters:
1. Monetization 
2. Engagement Retention 
3. New-user retention
4. Toxicity to the minimal

As such, model needs to be optimised based on: 
- Revenue
- Viewer Retention
- Community Growth
- Stream Flow

*NOTE:*<br>
If stream session has low number of viewers, ALL viewers should be entertained unless they're negative viewers.

## Priorities
### High value gifts must be acknowledged
These viewers are of utmost-priority as they contribute significantly to the value of stream with gifts. Bigger gifts are to be prioritised.

### Viewers with whale tags
Potential future monetization; Having interactive engagement with these group of viewers will show to the other viewers about the gifting culture publicly, enticing them to gift as well.

### New to stream Viewers
Even though they may be new or first time watching the stream, engaging with them will help with turning them into regular viewers and makes the stream session more engaging and welcoming to everyone. Having more viewers will increase the chances of getting gifts.

### Gift Mentions
Adds some priority for messages that contains the word "gift" as there might be potential for gifts to be involved.

### Requests from Viewers (with no gifting)
Keep viewers entertained and engaged. Lower priority as no monetization is involved.

### Negative/Toxic Viewers
To be ignored as they creates toxicity and negative vibes in the session, resulting in the stream being less welcoming and lesser viewers. Unless worsened, best to be ignored.

## System Architecture
Chat Stream<br>
↓<br>
Rule-Based Scoring<br>
↓<br>
Priority Ranking<br>
↓<br>
Top 3 Message Selection<br>
↓<br>
Single Batched LLM Request<br>
↓<br>
AI Reply Generation

## Filtering Strategy
### Rule-based filtering + LLM Replies
Instead of sending every livestream message to the LLM, the system first applies lightweight rule-based scoring.

This reduces:
- API cost
- latency
- unnecessary LLM calls

Only shortlisted high-priority messages are sent to the LLM for response generation.

#### Rule engine to score the messages
| Message           |  Score  | 
| ----------------- | ------- | 
| High Value Gift | 100 |
| Normal Gift | 60 |
| Whale Viewer | 40 |
| New Viewer | 30 |
| "Gift" mentions | 20 |
| Requests | 10 |
| Negative Viewer | -30 |
<br>
Prioritising gifts, whale users and new viewers. The rest takes lower priorities as it does not add monetization value, although they are crucial to maintain the stream flow.

## Human-Like Reply Generation

The system prompt was designed to imitate real livestream behavior:
- Short reactions
- Casual mix of language between Indonesian & English
- Imperfect grammar
- Playful streamer energy
- Spontaneous responses

The prompt intentionally avoids:
- Formal language
- Long explanations
- Overly polished AI responses

## How to run:
### 1. Create a ".env" file
Create a '.env' file in the root folder

### 2. ENTER API KEY
Inside the '.env' file, put in the following:<br>
OPENAI_API_KEY=your_key_here

### 3. Activate virtual environment
Enter the following in CMD/Bash:<br>
venv\Scripts\activate

### 4. Install Dependencies (in Virtual Env)
Run the following: <br>
pip install -r requirements.txt

### 5. Run app.py
- Open CMD/Bash
- Enter "python app.py"

## Output Images
### Following are the outputs after running app.py multiple times
#### Initial Run
Starts off with basic information displayed, such as the user, the message he/she sent, as well as the score allocated for the message. Only the top 3 messages are displayed.
![1](/assets/images/run1.png "Initial Run")

#### Added reasoning
Added information such as reasonings as to why they are being scored high for their messages.
![2](/assets/images/run4.png "Added Reasonings")

#### Added extra information 
Shows the number of messages processed, how many messages are sent to the LLM and runtime. Only top 3 messages are sent, with the rest filtered.
![3](/assets/images/run6.png "Statistics Display")

#### Faced with anomaly where runtime takes very long
Runtime of ~44 seconds. Was observed to be stuck at generating the third reply.
![4](/assets/images/anomaly-run7.png "Long Runtime")

#### Final Output
![5](/assets/images/fixed-reply-run10.png "Final Output")







## Enhancements & Fixes
- Changed encoding to UTF-8 to support Emojis
- Rectified prompts.py to ensure that the AI replies are more realistic than robot-like
- Added Reasoning to show why the messages are being selected
- Added timer to display runtime
- Added Statistics to show the details of data processing
- Added more chat messages to sample_chat to check performance (runtime)
- Discovered some anomaly where runtime would be unusually long (due to sequential LLM calls)
- Changed API Request from 3 to 1
- Fixed reply formatting