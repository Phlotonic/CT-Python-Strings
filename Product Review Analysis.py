# Task 1: Keyword Highlighter
def highlight_keywords(reviews):
    keywords = ["good", "excellent", "bad", "poor", "average"]
    highlighted_reviews = []
    
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        highlighted_reviews.append(review)
    
    return highlighted_reviews

# Task 2: Sentiment Tally
def sentiment_tally(reviews, positive_words, negative_words):
    positive_count = 0
    negative_count = 0
    
    for review in reviews:
        for word in positive_words:
            positive_count += review.lower().count(word)
        for word in negative_words:
            negative_count += review.lower().count(word)
    
    return positive_count, negative_count

# Task 3: Review Summary
def summarize_reviews(reviews):
    summaries = []
    
    for review in reviews:
        if len(review) > 30:
            # Ensure the summary does not cut off in the middle of a word
            summary = review[:30].rsplit(' ', 1)[0] + "…"
        else:
            summary = review
        summaries.append(summary)
    
    return summaries

# Sample data
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Execute Task 1
highlighted_reviews = highlight_keywords(reviews)
print("Highlighted Reviews:")
for review in highlighted_reviews:
    print(review)

# Execute Task 2
positive_count, negative_count = sentiment_tally(reviews, positive_words, negative_words)
print("\nSentiment Tally:")
print(f"Positive words count: {positive_count}")
print(f"Negative words count: {negative_count}")

# Execute Task 3
summaries = summarize_reviews(reviews)
print("\nReview Summaries:")
for summary in summaries:
    print(summary)

