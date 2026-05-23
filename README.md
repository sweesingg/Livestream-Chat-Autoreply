# Livestream Chat Autoreply
For streamers to reply effectively and as real as possible

## Context
Streamers reply to about 8% of chat messages.<br>
Only 42% of gifts get acknowledged within 30 seconds — the goal is 80%+.

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

### Requests from Viewers (with no gifting)
More for keeping the viewers entertained and engaged, keeping the session fun. Lower priority as no monetization is involved.

### Negative/Toxic Viewers
To be ignored as they creates toxicity and negative vibes in the session, resulting in the stream being less welcoming and lesser viewers. Unless worsened, best to be ignored.

## Anti Robotic Replies
To ensure that the replies are not robotic, suggestive replies will appear on the streamer's screen, allowing the streamer to select which texts they want to reply to the chat. This serves as a shortcut, as well as having the streamer ensuring that the replies are good. 
<br><br>
Furthermore, these suggestive replies can be changed to customisable, allowing users to make minimal changes to it.<br>
Nonetheless, streamers have the option to fully automate the reply, although they might be subjected to more non-humanlike replies.
<br><br>
Ultimately, authenticity is the key for such replies.

## Filtering Strategy
### Rule-based filtering + LLM Replies
#### Step 1: Have a rule engine to score the messages
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

#### Step 2: Weigh and generate replies only for the top 3 messages
Requirements for replies:
- Mix of Indonesian + English 
- Playful and warm


## How to run:
### 1. Create a ".env" file
Create a '.env' file in the root folder

### 2. ENTER API KEY
Inside the '.env' file, put in the following:<br>
OPENAI_API_KEY=your_key_here

### 3. Activate virtual environment
Enter the following in CMD/Bash:<br>
venv\Scripts\activate

### 3. Install Dependencies (in Virtual Env)
Run the following: <br>
pip install -r requirements.txt

### 4. Run app.py
- Open CMD/Bash
- Enter "python app.py"


## Output Images
### Following are the outputs after running app.py multiple times
#### Run 1
![Sample Test Run 1](/assets/images/run1.png "First Run")
#### Run 2
![Sample Test Run 2](/assets/images/run2.png "Second Run")
#### Run 3
![Sample Test Run 3](/assets/images/run3.png "Third Run")

## Refinements
### Changed encoding to UTF-8 to support Emojis
### Rectified prompts.py to ensure that the AI replies are more realistic than robot-like
### Added Reasoning to show why the messages are being selected
### Added timer to display runtime
### Added Statistics to show the details of data processing
### Added more chat messages to sample_chat to check performance (runtime)
### Discovered some anomaly where runtime would be unusually long (due to sequential LLM calls)
### Changed API Request from 3 to 1
### Fixed reply formatting