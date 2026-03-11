from google.cloud import bigquery

client = bigquery.Client()

youtube_table_id = "your_project.your_dataset.youtube_fact"
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
)
with open("data/youtube_trending.csv", "rb") as source_file:
    job = client.load_table_from_file(source_file, youtube_table_id, job_config=job_config)
job.result()
print("✅ YouTube data loaded into BigQuery")

news_table_id = "your_project.your_dataset.news_fact"
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
)
with open("data/cleaned_news.csv", "rb") as source_file:
    job = client.load_table_from_file(source_file, news_table_id, job_config=job_config)
job.result()
print("✅ News data loaded into BigQuery")
