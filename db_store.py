"""
Push a DataFrame into the DB.
`python db_store.py` will fetch fresh data and append it.
"""
from sqlalchemy import create_engine
from fetch_data import fetch_crypto_data
from config import DATABASE_URL

def store_data(df):
    engine = create_engine(DATABASE_URL)
    with engine.begin() as conn:          # autocommit
        df.to_sql("crypto_prices", conn, if_exists="append", index=False)
    print(f"Inserted {len(df)} rows ✅")

if __name__ == "__main__":
    store_data(fetch_crypto_data())
