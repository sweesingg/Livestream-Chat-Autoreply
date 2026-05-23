def score_message(msg):
    score = 0
    reasons = []

    if msg.get("gift") == "yes":
        if msg.get("gift_value", 0) >= 300:
            score += 100
            reasons.append("High-value gift")
        else:
            score += 60
            reasons.append("Normal gift")
    
    if msg.get("type") == "whale":
        score += 40
        reasons.append("Whale user")

    if msg.get("type") == "new_user":
        score += 30
        reasons.append("New user")

    if msg.get("ongoing_request") == "yes":
        score += 10
        reasons.append("Ongoing request")

    if "gift" in msg["message"].lower():
        score += 20
        reasons.append("Message contains 'gift'")
    
    negative_comments = ["boring", "stupid"]

    if any(word in msg["message"] for word in negative_comments):
        score -= 30
        reasons.append("Message contains negative comments")
    # need to cater to unanswered messages

    return score, reasons