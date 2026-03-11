CREATE TABLE youtube_fact (
    content_id STRING,
    channel_id STRING,
    channel_title STRING,
    category_id STRING,
    category_name STRING,
    views INT64,
    likes INT64,
    like_ratio FLOAT64,
    published_date DATE
);

CREATE TABLE news_fact (
    article_id STRING,
    category STRING,
    year INT64,
    clean_text STRING
);

CREATE TABLE category_dim (
    category_id STRING,
    category_name STRING,
    source STRING
);
