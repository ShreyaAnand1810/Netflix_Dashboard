# app.py
import streamlit as st
import plotly.express as px
import pandas as pd
from data import load_raw, preprocess, get_summaries

st.set_page_config(page_title="Netflix Shows & Movies Analytics", layout="wide", initial_sidebar_state="expanded")

@st.cache_data
def load_and_prep(path="Data/netflix_titles.csv"):
    raw = load_raw(path)
    df = preprocess(raw)
    return df

# --- Load data ---
st.title("Netflix Shows & Movies Analytics")
st.caption("Interactive dashboard — filter and explore content release trends and distributions.")

df = load_and_prep()

# Summary cards
sums = get_summaries(df)
col1, col2, col3, col4 = st.columns([1,1,1,2])
col1.metric("Rows (records)", sums["n_rows"])
col2.metric("Movies", sums["n_movies"])
col3.metric("TV Shows", sums["n_shows"])
yr_range = sums["years_range"]
col4.write(f"Release years range: **{yr_range[0]}** — **{yr_range[1]}**")

# --- Sidebar filters ---
st.sidebar.header("Filters")
# Year range slider (based on release_year_int)
min_year = int(df["release_year_int"].min()) if df["release_year_int"].notna().any() else 1900
max_year = int(df["release_year_int"].max()) if df["release_year_int"].notna().any() else 2025
yr_sel = st.sidebar.slider("Release year range", min_year, max_year, (min_year, max_year))

# Type select
types = ["All"] + sorted(df["type"].dropna().unique().tolist())
typ = st.sidebar.selectbox("Type", types, index=0)

# Country multi-select
countries = sorted([c for c in df["primary_country"].dropna().unique()])
country_sel = st.sidebar.multiselect("Primary country (choose 0..n)", options=countries, default=[])

# Genre multi-select (primary genre)
genres = sorted([g for g in df["primary_genre"].dropna().unique()])
genre_sel = st.sidebar.multiselect("Primary genre", options=genres, default=[])

# Title search
title_search = st.sidebar.text_input("Search title (contains)")

# Apply filters
filtered = df.copy()
filtered = filtered[filtered["release_year_int"].between(yr_sel[0], yr_sel[1], inclusive="both")]

if typ != "All":
    filtered = filtered[filtered["type"] == typ]

if country_sel:
    filtered = filtered[filtered["primary_country"].isin(country_sel)]

if genre_sel:
    filtered = filtered[filtered["primary_genre"].isin(genre_sel)]

if title_search and title_search.strip():
    filtered = filtered[filtered["title"].str.contains(title_search.strip(), case=False, na=False)]

st.sidebar.markdown(f"**Results:** {len(filtered):,} records")

# --- Main layout: charts + table ---
st.subheader("Overview charts")

# Releases per year (line)
with st.container():
    st.markdown("**Number of releases per year**")
    releases = (
        filtered.groupby("release_year_int")
                .size()
                .reset_index(name="count")
                .dropna()
                .sort_values("release_year_int")
    )
    if len(releases) > 0:
        fig = px.line(releases, x="release_year_int", y="count", markers=True,
                      labels={"release_year_int":"Release Year", "count":"Number of titles"})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data for chosen filters")

# Type distribution
with st.container():
    st.markdown("**Type distribution (Movies vs TV Shows)**")
    type_counts = filtered["type"].value_counts().reset_index()
    type_counts.columns = ["type", "count"]
    if not type_counts.empty:
        fig2 = px.pie(type_counts, names="type", values="count", hole=0.3)
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("No data for chosen filters")

# Top countries
with st.container():
    st.markdown("**Top countries by number of titles**")
    top_countries = (
        filtered.groupby("primary_country")
                .size()
                .reset_index(name="count")
                .dropna()
                .sort_values("count", ascending=False)
                .head(15)
    )
    if not top_countries.empty:
        fig3 = px.bar(top_countries, x="primary_country", y="count", labels={"primary_country":"Country", "count":"Number of titles"})
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.info("No data for chosen filters")

# Genre heatmap across years (pivot)
with st.container():
    st.markdown("**Top genres over time (heatmap)** — use 'Primary Genre' for simplicity")
    # limit to top genres in filtered set
    gcounts = filtered["primary_genre"].value_counts().head(10).index.tolist()
    heat_df = filtered[filtered["primary_genre"].isin(gcounts)].groupby(["release_year_int", "primary_genre"]).size().reset_index(name="count")
    if not heat_df.empty:
        pivot = heat_df.pivot_table(index="primary_genre", columns="release_year_int", values="count", fill_value=0)
        # convert pivot to long form for plotly
        pivot_long = pivot.reset_index().melt(id_vars="primary_genre", var_name="year", value_name="count")
        fig4 = px.density_heatmap(pivot_long, x="year", y="primary_genre", z="count", labels={"primary_genre":"Genre", "year":"Year", "count":"Number"})
        st.plotly_chart(fig4, use_container_width=True)
    else:
        st.info("No data for chosen filters")

# --- Table of results with quick actions ---
st.subheader("Filtered titles")
# show a compact table with title, type, year, country, genre, brief description, and action button (open netflix search)
def make_display_table(df_in: pd.DataFrame) -> pd.DataFrame:
    disp = df_in[["title", "type", "release_year_int", "primary_country", "primary_genre", "description", "netflix_search_url"]].copy()
    disp = disp.rename(columns={
        "release_year_int":"year",
        "primary_country":"country",
        "primary_genre":"genre",
        "netflix_search_url":"netflix_url"
    })
    # Shorten description for table
    disp["description"] = disp["description"].str.slice(0, 140) + disp["description"].str.len().map(lambda x: "..." if x > 140 else "")
    return disp

disp_table = make_display_table(filtered)

# show top 50 results
max_show = st.slider("Max results to show", min_value=5, max_value=200, value=50)
st.dataframe(disp_table.head(max_show), use_container_width=True)

# Provide per-row action links below the table
st.markdown("### Quick open (first 20)")
for _, row in disp_table.head(20).iterrows():
    title = row["title"]
    url = row["netflix_url"]
    year = row["year"]
    if url:
        st.markdown(f"- **{title}** ({year}) — [Open on Netflix]({url})")
    else:
        st.markdown(f"- **{title}** ({year}) — no link available")

st.markdown("---")
st.caption("Tip: clicking 'Open on Netflix' sends you to Netflix search results for that title. Netflix will ask you to sign in to watch the content.")



