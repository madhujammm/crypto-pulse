"""
Pull data from CoinGecko API and return a pandas DataFrame.
Run directly to print a preview.
"""
import requests
import pandas as pd
from datetime import datetime
from config import API_URL, API_PARAMS

def fetch_crypto_data() -> pd.DataFrame:
    resp = requests.get(API_URL, params=API_PARAMS, timeout=15)
    resp.raise_for_status()          # explode loudly if API is down
    data = resp.json()

    # keep only fields we care about
    cols = [
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_percentage_24h"
    ]
    df = pd.DataFrame(data)[cols]

    # cleaning / enrichment
    df.columns = [c.upper() for c in df.columns]
    df["FETCHED_AT"] = datetime.utcnow()

    # enforce types
    numeric_cols = ["CURRENT_PRICE", "MARKET_CAP", "TOTAL_VOLUME", "PRICE_CHANGE_PERCENTAGE_24H"]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

    return df.dropna()

if __name__ == "__main__":
    print(fetch_crypto_data().head())
