# src/collect.py
# Scraper stub: downloads the Wikipedia page and extracts the first wikitable.
# Requires internet; run this locally to fetch the live dataset.
import requests
from bs4 import BeautifulSoup
import pandas as pd

WIKI_URL = "https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes"

def fetch_table():
    resp = requests.get(WIKI_URL)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    tables = soup.find_all("table", {"class": "wikitable"})
    if not tables:
        raise RuntimeError("No wikitable found on page")
    df = pd.read_html(str(tables[0]))[0]
    return df

if __name__ == "__main__":
    df = fetch_table()
    df.to_csv("data/prison_escapes_raw.csv", index=False)
    print("Saved data/prison_escapes_raw.csv")
