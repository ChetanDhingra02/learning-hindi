"""Loads and searches the full 144k-word English-Hindi dictionary."""
import os
import pandas as pd
import streamlit as st

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "full_dictionary.csv")


@st.cache_data(show_spinner=False)
def load_dictionary():
    df = pd.read_csv(DATA_PATH)
    df["english"] = df["english"].astype(str)
    df["hindi"] = df["hindi"].astype(str)
    df["translit"] = df["translit"].astype(str)
    df["pos"] = df["pos"].astype(str)
    return df


def search_dictionary(df, query, pos_filter=None, limit=200):
    if not query or not query.strip():
        return df.iloc[0:0]
    q = query.strip().lower()
    mask = (
        df["english"].str.lower().str.contains(q, regex=False)
        | df["hindi"].str.contains(query.strip(), regex=False)
        | df["translit"].str.lower().str.contains(q, regex=False)
    )
    result = df[mask]
    if pos_filter and pos_filter != "All":
        result = result[result["pos"] == pos_filter]
    # rank: exact english match first, then startswith, then contains
    exact = result[result["english"].str.lower() == q]
    starts = result[result["english"].str.lower().str.startswith(q) & (result["english"].str.lower() != q)]
    rest = result[~result["english"].str.lower().str.startswith(q)]
    ordered = pd.concat([exact, starts, rest])
    return ordered.head(limit)


def word_of_the_day(df, seed_key):
    """Deterministic-ish pick based on a seed string (e.g. today's date)."""
    idx = abs(hash(seed_key)) % len(df)
    return df.iloc[idx]
