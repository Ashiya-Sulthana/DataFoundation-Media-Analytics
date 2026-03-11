import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

df = pd.read_csv("data/news.csv")

df.dropna(subset=["text"], inplace=True)
df["category"] = df["category"].str.strip().str.lower()

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["year"] = df["date"].dt.year

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return " ".join(tokens)

df["clean_text"] = df["text"].apply(clean_text)

df.to_csv("data/cleaned_news.csv", index=False)
print("✅ Cleaned news dataset saved to data/cleaned_news.csv")
