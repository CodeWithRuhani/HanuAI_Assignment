import pandas as pd
import re
import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# -----------------------------
# TEXT PREPROCESSING
# -----------------------------
def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r"[^\w\s]", "", text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)


# -----------------------------
# TAG EXTRACTION (TF-IDF)
# -----------------------------
def extract_tags(df, text_column):
    print("🔹 Preprocessing text...")

    df["processed_text"] = df[text_column].apply(preprocess_text)

    print("🔹 Applying TF-IDF...")

    tfidf = TfidfVectorizer(max_features=50)
    X = tfidf.fit_transform(df["processed_text"])

    terms = tfidf.get_feature_names_out()

    def get_top_terms(row):
        indices = row.toarray()[0].argsort()[-5:]
        return [terms[i] for i in indices]

    df["tags"] = [get_top_terms(X[i]) for i in range(X.shape[0])]

    return df, X


# -----------------------------
# CLUSTERING (KMeans)
# -----------------------------
def cluster_issues(df, X):
    print("🔹 Clustering issues...")

    kmeans = KMeans(n_clusters=4, random_state=42)
    df["issue_category"] = kmeans.fit_predict(X)

    return df


# -----------------------------
# MAIN EXECUTION
# -----------------------------
if __name__ == "__main__":
    print("🔹 Loading cleaned data...")

    df = pd.read_csv("../data/cleaned_data.csv")

    # 👇 IMPORTANT: Using correct column
    df, X = extract_tags(df, text_column="customer_verbatim")

    df = cluster_issues(df, X)

    df.to_csv("../data/tagged_data.csv", index=False)

    print("\n✅ Tagged data saved to: ../data/tagged_data.csv")