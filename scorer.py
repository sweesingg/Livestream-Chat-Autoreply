def score_message(msg):
    score = 0

    if msg.get("gift") == "yes":
        if msg.get("gift_value", 0) >= 300:
            score += 100
        else:
            score += 60
    
    if msg.get("type") == "whale":
        score += 40

    if msg.get("type") == "new_user":
        score += 30
    
    if msg.get("ongoing_request") == "yes":
        score += 10

    if "gift" in msg["message"].lower():
        score += 20
    
    negative_comments = ["boring", "stupid"]

    if any(word in msg["message"] for word in negative_comments):
        score -= 30
    # need to cater to unanswered messages

    return score