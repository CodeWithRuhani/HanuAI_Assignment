import pandas as pd
from bs4 import BeautifulSoup

def scrape_from_html(file_path, max_reviews=50):
    print("Reading HTML file...")

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    reviews = []

    # Try multiple possible selectors
    review_blocks = soup.find_all("div")

    print(f"Total divs found: {len(review_blocks)}")

    for r in review_blocks:
        text = r.get_text(strip=True)

        # Heuristic: pick divs that look like reviews
        if text and len(text) > 100:  # filter small divs
            try:
                reviews.append({
                    "id": len(reviews) + 1,
                    "title": "",
                    "text": text,
                    "rating": "",
                    "reviewer": "",
                    "date": "",
                    "source": "BestBuy"
                })
            except:
                continue

        if len(reviews) >= max_reviews:
            break

    df = pd.DataFrame(reviews)

    print(f"Extracted {len(df)} possible reviews")

    return df


if __name__ == "__main__":
    df = scrape_from_html("../data/reviews.html")
    df.to_csv("../data/raw_reviews.csv", index=False)
    print("Saved to raw_reviews.csv")