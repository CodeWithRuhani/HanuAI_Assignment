import pandas as pd
import nltk
import re
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

def clean_text(text):
    if pd.isna(text):
        return ""
    
    text = text.lower()
    text = re.sub(r"http\S+", "", text)      # remove links
    text = re.sub(r"[^a-zA-Z\s]", "", text) # remove special chars
    text = re.sub(r"\s+", " ", text).strip()
    
    return text

def analyze_sentiment(text):
    score = sia.polarity_scores(text)["compound"]

    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def process_reviews(input_path, output_path):
    print("Loading raw data...")
    df = pd.read_csv(input_path)

    print("Cleaning text...")
    df["clean_text"] = df["text"].apply(clean_text)

    print("Removing empty/short rows...")
    df = df[df["clean_text"].str.len() > 20]

    print("Applying sentiment analysis...")
    df["sentiment"] = df["clean_text"].apply(analyze_sentiment)

    print("Saving processed data...")
    df.to_csv(output_path, index=False)

    print("Done!")

if __name__ == "__main__":
    process_reviews(
        "../data/raw_reviews.csv",
        "../data/processed_reviews.csv"
    )