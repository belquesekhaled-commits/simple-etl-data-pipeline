import logging
import sqlite3
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "raw_sales_data.csv"
OUTPUT_PATH = BASE_DIR / "data" / "cleaned_sales_data.csv"
DB_PATH = BASE_DIR / "sales.db"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def extract(csv_file: Path) -> pd.DataFrame:
    logging.info("Extracting data from CSV...")
    df = pd.read_csv(csv_file)
    logging.info("Loaded %s rows.", len(df))
    return df

def transform(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Transforming data...")

    # Remove rows with missing price
    df = df.dropna(subset=["price"]).copy()

    # Remove exact duplicates
    df = df.drop_duplicates()

    # Standardize text columns
    text_cols = ["customer_name", "product", "category", "city"]
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip()

    # Convert types
    df["price"] = df["price"].astype(float)
    df["quantity"] = df["quantity"].astype(int)
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Add calculated column
    df["total_amount"] = df["price"] * df["quantity"]

    # Add month column for analysis
    df["order_month"] = df["order_date"].dt.to_period("M").astype(str)

    logging.info("Data transformed successfully. Remaining rows: %s", len(df))
    return df

def load(df: pd.DataFrame, db_file: Path, output_csv: Path) -> None:
    logging.info("Loading data into SQLite database...")
    conn = sqlite3.connect(db_file)
    try:
        df.to_sql("sales_cleaned", conn, if_exists="replace", index=False)
        logging.info("Loaded cleaned data into table: sales_cleaned")
    finally:
        conn.close()

    df.to_csv(output_csv, index=False)
    logging.info("Saved cleaned CSV to %s", output_csv)

def main() -> None:
    df = extract(DATA_PATH)
    df_clean = transform(df)
    load(df_clean, DB_PATH, OUTPUT_PATH)
    logging.info("ETL process completed successfully.")

if __name__ == "__main__":
    main()