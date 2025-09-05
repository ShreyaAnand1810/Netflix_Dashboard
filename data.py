# data.py
import pandas as pd
from dateutil import parser
from typing import Tuple
import urllib.parse

CSV_PATH = "Data/netflix_titles.csv"

def load_raw(csv_path: str = CSV_PATH) -> pd.DataFrame:
    """
    Load the Netflix CSV into a DataFrame.
    """
    df = pd.read_csv(csv_path)
    return df

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleaning:
    - Parse date_added to datetime if present and create date_added_year
    - Ensure release_year column exists
    - Normalize type, country, listed_in (genres)
    - Fill missing values for convenience
    - Create a netflix_search_url for quick redirection (search by title)
    """
    df = df.copy()
    # Standardize column names (strip)
    df.columns = [c.strip() for c in df.columns]

    # Parse date_added
    if "date_added" in df.columns:
        def parse_date(x):
            try:
                return parser.parse(x) if pd.notna(x) else pd.NaT
            except Exception:
                return pd.NaT
        df["date_added_parsed"] = df["date_added"].astype(str).replace("nan", pd.NA).map(lambda x: parse_date(x) if pd.notna(x) else pd.NaT)
        df["date_added_year"] = df["date_added_parsed"].dt.year
    else:
        df["date_added_parsed"] = pd.NaT
        df["date_added_year"] = pd.NA

    # release_year fallback
    if "release_year" not in df.columns:
        df["release_year"] = pd.NA
    else:
        df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce").astype("Int64")

    # Normalize textual columns
    for col in ["type", "country", "listed_in", "title", "director", "cast", "rating", "duration", "description"]:
        if col not in df.columns:
            df[col] = pd.NA

    # Split countries and genres into lists for filtering
    df["country_list"] = df["country"].fillna("").map(lambda s: [c.strip() for c in s.split(",")] if s else [])
    df["genre_list"] = df["listed_in"].fillna("").map(lambda s: [g.strip() for g in s.split(",")] if s else [])

    # Extract primary country and primary genre for grouping convenience
    df["primary_country"] = df["country_list"].map(lambda lst: lst[0] if lst else pd.NA)
    df["primary_genre"] = df["genre_list"].map(lambda lst: lst[0] if lst else pd.NA)

    # netflix search url — redirects to netflix search page for the title
    def netflix_search_url(title: str) -> str:
        if pd.isna(title) or str(title).strip() == "":
            return ""
        q = urllib.parse.quote_plus(str(title))
        return f"https://www.netflix.com/search?q={q}"

    df["netflix_search_url"] = df["title"].map(lambda t: netflix_search_url(t))

    # release year as int where possible (for timeline plots)
    try:
        df["release_year_int"] = pd.to_numeric(df["release_year"], errors="coerce").astype("Int64")
    except Exception:
        df["release_year_int"] = pd.NA

    # Short description safe string
    df["description"] = df["description"].fillna("No description available")

    return df

def get_summaries(df: pd.DataFrame) -> dict:
    """
    small metadata summaries used in dashboard header
    """
    return {
        "n_rows": len(df),
        "n_movies": int((df["type"] == "Movie").sum()) if "type" in df.columns else None,
        "n_shows": int((df["type"] == "TV Show").sum()) if "type" in df.columns else None,
        "years_range": (int(df["release_year_int"].min()) if df["release_year_int"].notna().any() else None,
                        int(df["release_year_int"].max()) if df["release_year_int"].notna().any() else None)
    }


