# AI Usage Log

This document summarizes how AI assistance was used during the development of the AI Livestream Chat Copilot assignment.

AI was primarily used as:
- a development assistant,
- debugging support tool,
- architecture brainstorming tool,
- and prompt refinement assistant.

The final implementation, project structure, prioritization logic, and system integration decisions were manually reviewed and implemented.

---

# AI-Assisted Tasks

## 1. Project Planning & Architecture

AI assistance was used to:
- brainstorm the overall system structure,
- separate rule-based scoring from LLM generation,
- design the modular file structure (`app.py`, `scorer.py`, `prompts.py`),
- and discuss scalable filtering strategies.

Key architectural ideas explored:
- rule-based filtering before LLM calls,
- batching shortlisted messages into a single API request,
- reducing latency and API overhead,
- explainable priority scoring.

---

## 2. Prompt Engineering

AI assistance was used to:
- refine the livestream personality prompt,
- improve human-like streamer responses,
- reduce robotic or overly formal phrasing,
- and tune reply length and tone.

Prompt iterations focused on:
- Indonesian-English code switching,
- short livestream-style replies,
- reducing overly “AI-generated” sounding responses,
- and improving spontaneity/authenticity.

---

## 3. Debugging & Error Resolution

AI assistance was used to troubleshoot:
- UTF-8 encoding issues,
- OpenAI API authentication setup,
- `.env` configuration,
- Git and `.gitignore` issues,
- virtual environment setup,
- JSON loading errors,
- and batched API response formatting/parsing.

---

## 4. Performance Optimization

AI assistance was used to:
- analyze inconsistent runtime performance,
- identify sequential API calls as the bottleneck,
- and refactor the system into a single batched LLM request.

This optimization reduced runtime significantly and improved scalability.

---

# Prompt Iteration Summary

Examples of prompt refinement themes explored during development:

- Making replies sound less robotic
- Shortening generated responses
- Encouraging casual livestream tone
- Avoiding long AI-generated paragraphs
- Improving Indo-English conversational style
- Preventing over-generated lyrics
- Structuring batched reply formatting
- Improving parsing reliability using separators

---

# Development Approach

The project intentionally combines:
- lightweight rule-based heuristics,
- explainable scoring logic,
- and LLM-based natural language generation.

This hybrid approach was chosen to better simulate how real-time livestream systems prioritize responsiveness, scalability, and human-like interaction quality.

---

# Prompts used with AI

1. Elaborate more on the different AI System Designs

2. Analyse these chat texts. Show me some of the replies that should be generate such that it would not sound like a chatbot.
Add in mixes of Indonesian and English in casual conversion and with energy.

3. Suggest some tones that will make the reply more energetic, friendly and engaging.

4. Show me examples of how the flow should be like, using Rule-based filtering + LLM Replies

5. What files do I need?

6. How to make the replies generated more authentic, real time and less ai-generated replies?

7. [Attached image of output] How to further improve the response?

8. How do i initialise a timer here? 

9. What are some of the statistics that is useful to show? 

10. How do I combine the individual API calls into one ?

11. Checking if prompts.py can be removed since the combined API call already defined some rules

