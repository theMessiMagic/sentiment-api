from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CommentRequest(BaseModel):
    comment: str

def analyze_sentiment(text: str):
    text = text.lower()

    positive_words = ["amazing", "great", "good", "excellent", "love", "fantastic", "awesome", "best"]
    negative_words = ["bad", "terrible", "worst", "awful", "hate", "poor", "disappointing"]

    score = 3  # neutral base

    for word in positive_words:
        if word in text:
            score += 1

    for word in negative_words:
        if word in text:
            score -= 1

    # clamp rating between 1 and 5
    score = max(1, min(5, score))

    if score >= 4:
        sentiment = "positive"
    elif score <= 2:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {
        "sentiment": sentiment,
        "rating": score
    }

@app.get("/comment")
async def analyze_comment(data: CommentRequest):
    return analyze_sentiment(data.comment)
