import pandas as pd
from googleapiclient.discovery import build

with open("keys/youtube_api_key.txt") as f:
    api_key = f.read().strip()

youtube = build("youtube", "v3", developerKey=api_key)

video_request = youtube.videos().list(
    part="snippet,statistics",
    chart="mostPopular",
    maxResults=10,
    regionCode="IN"
)
video_response = video_request.execute()

metrics = []
for item in video_response["items"]:
    views = int(item["statistics"].get("viewCount", 0))
    likes = int(item["statistics"].get("likeCount", 0))
    metrics.append({
        "content_id": item["id"],
        "channel_id": item["snippet"]["channelId"],
        "channel_title": item["snippet"]["channelTitle"],
        "category_id": item["snippet"]["categoryId"],
        "views": views,
        "likes": likes,
        "like_ratio": round(likes / views, 4) if views > 0 else 0,
        "published_date": item["snippet"]["publishedAt"].split("T")[0]
    })

cat_request = youtube.videoCategories().list(part="snippet", regionCode="IN")
cat_response = cat_request.execute()
cat_map = {item["id"]: item["snippet"]["title"] for item in cat_response["items"]}

for m in metrics:
    m["category_name"] = cat_map.get(m["category_id"], "Unknown")

df = pd.DataFrame(metrics)
df.to_csv("data/youtube_trending.csv", index=False)
print("✅ YouTube trending data saved to data/youtube_trending.csv")
