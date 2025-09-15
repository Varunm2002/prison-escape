# src/clean.py
import pandas as pd

def clean(df):
    df = df.copy()
    df.columns = [c.strip() for c in df.columns]
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    # Normalize Success column if present
    if 'Success' in df.columns:
        df['Success'] = df['Success'].astype(str).str.strip()
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/prison_escapes_raw.csv")
    df = clean(df)
    df.to_csv("data/prison_escapes.csv", index=False)
    print("Saved cleaned data/prison_escapes.csv")
