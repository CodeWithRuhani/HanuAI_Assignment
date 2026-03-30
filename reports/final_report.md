# HanuAI ML Assignment Report

---

## 1. Introduction

This project focuses on extracting meaningful insights from customer reviews and structured datasets using data analysis and NLP techniques. The objective is to identify patterns, customer sentiments, and common issues to provide actionable business recommendations.

---

## 2. Task 1: Web Scraping & Sentiment Analysis

### Approach
- Scraped product reviews from BestBuy using a hybrid approach due to anti-scraping restrictions.
- Extracted key fields such as review text, rating, reviewer, and date.
- Cleaned text data and applied sentiment analysis using NLTK VADER.

### Challenges
- BestBuy blocked automated scraping using Selenium (Akamai protection).
- Resolved using a hybrid approach by parsing rendered HTML.

### Key Insights
- Majority of reviews were **Positive**, indicating overall customer satisfaction.
- Positive feedback focused on:
  - Product quality
  - Performance
  - Ease of use
- Negative feedback highlighted:
  - Price concerns
  - Durability issues

---

## 3. Task 2: EDA & Text Mining

### Approach
- Cleaned dataset by handling missing values and duplicates.
- Performed exploratory data analysis to understand patterns.
- Applied NLP techniques:
  - Text preprocessing
  - TF-IDF for keyword extraction
  - KMeans clustering for grouping similar issues

### Key Insights
- Most frequent issues relate to **component failures** and **electrical problems**.
- Clustering revealed recurring complaint patterns across multiple entries.
- Many structured columns had missing values, indicating gaps in data collection.

---

## 4. Business Recommendations

- Improve quality control for frequently failing components.
- Focus on resolving recurring issues identified through clustering.
- Enhance data collection mechanisms for better tracking of failure conditions.
- Use NLP-based monitoring systems to detect issues early from customer feedback.

---

## 5. Conclusion

The analysis successfully transformed raw and unstructured data into actionable insights. The combination of EDA and NLP techniques provides a scalable approach for monitoring product performance and improving customer satisfaction.

---