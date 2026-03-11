import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Media Analytics Dashboard", layout="wide")
st.title("📊 Media Content Analytics Platform")

df_channels = pd.read_csv("data/youtube_trending.csv")
df_clean = pd.read_csv("data/cleaned_news.csv")

st.sidebar.header("🔎 Filters")

selected_channels = st.sidebar.multiselect("Select Channel(s)", df_channels["channel_title"].unique(), df_channels["channel_title"].unique())
df_channels_filtered = df_channels[df_channels["channel_title"].isin(selected_channels)]

selected_youtube_categories = st.sidebar.multiselect(
    "Select YouTube Category(s)",
    df_channels["category_name"].unique(),
    df_channels["category_name"].unique()
)
df_channels_filtered = df_channels[
    (df_channels["channel_title"].isin(selected_channels)) &
    (df_channels["category_name"].isin(selected_youtube_categories))
]

selected_kaggle_categories = st.sidebar.multiselect("Select Kaggle Category(s)", df_clean["category"].unique(), df_clean["category"].unique())
df_clean_filtered = df_clean[df_clean["category"].isin(selected_kaggle_categories)]

col1, col2, col3, col4 = st.columns(4)
col1.metric("👁 Views", f"{df_channels_filtered['views'].sum():,}")
col2.metric("👍 Likes", f"{df_channels_filtered['likes'].sum():,}")
col3.metric("🎥 Videos", f"{df_channels_filtered['content_id'].nunique():,}")
col4.metric("📰 Articles", f"{df_clean_filtered.shape[0]:,}")

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Channel (YouTube)")
    st.plotly_chart(
        px.bar(df_channels_filtered, x="channel_title", y="views", color="channel_title",
               color_discrete_sequence=px.colors.qualitative.Set3),
        use_container_width=True
    )

with col2:
    st.subheader("Category (YouTube)")
    st.plotly_chart(
        px.pie(df_channels_filtered, names="category_name", values="views", hole=0.4,
               color_discrete_sequence=px.colors.qualitative.Set3),
        use_container_width=True
    )

with col3:
    st.subheader("Articles per Year (Kaggle)")
    st.plotly_chart(
        px.bar(df_clean_filtered.groupby("year").size().reset_index(name="articles"),
               x="year", y="articles", color="year",
               color_discrete_sequence=px.colors.qualitative.Set3),
        use_container_width=True
    )

with col4:
    st.subheader("Articles Category (Kaggle)")
    st.plotly_chart(
        px.pie(df_clean_filtered, names="category", hole=0.4,
               color_discrete_sequence=px.colors.qualitative.Set3),
        use_container_width=True
    )
