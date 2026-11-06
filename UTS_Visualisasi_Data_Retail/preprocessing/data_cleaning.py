from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "dataset" / "supermarket_sales.csv"
OUTPUT = ROOT / "dataset" / "supermarket_sales_clean.csv"

def clean_data():
    df = pd.read_csv(SOURCE)
    df.columns = [c.strip() for c in df.columns]
    df = df.drop_duplicates()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    numeric = ["Unit price", "Quantity", "Tax 5%", "Total", "cogs",
               "gross margin percentage", "gross income", "Rating"]
    for col in numeric:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["Date", "Total", "Quantity"])
    df.to_csv(OUTPUT, index=False)
    print(f"Data bersih tersimpan: {OUTPUT}")
    print(f"Jumlah baris: {len(df)}")
    return df

if __name__ == "__main__":
    clean_data()
