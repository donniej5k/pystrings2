#task 1
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

def highlight_keywords(review, keywords):
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())
    return review

for review in reviews:
    print(highlight_keywords(review, keywords))

# Task 2

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def sentiment_tally(review, positive_words, negative_words):
    positive_count = 0
    negative_count = 0
    words = review.lower().split()

    for word in words:
        word = word.strip(".,!?")
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1

    return positive_count, negative_count

for review in reviews:
    pos_count, neg_count = sentiment_tally(review, positive_words, negative_words)
    print(f"Review: \"{review}\"")
    print(f"Positive words: {pos_count}, Negative words: {neg_count}\n")

# Task 3


def create_summary(review, max_length=30):
    if len(review) <= max_length:
        return review
    else:
        summary = review[:max_length]
        if review[max_length] != ' ':
            last_space = summary.rfind(' ')
            if last_space != -1:
                summary = summary[:last_space]
        return summary + "…"

for review in reviews:
    summary = create_summary(review)
    print(f"Review Summary: \"{summary}\"")
