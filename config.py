"""
Centralised config.
Edit DATABASE_URL or put it in a .env file as DATABASE_URL=sqlite:///crypto_data.db
"""
import os
from dotenv import load_dotenv
load_dotenv()

# CoinGecko endpoint & params
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
API_PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,     # top 50 coins
    "page": 1,
    "sparkline": False
}

# DB connection string (SQLite by default)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///crypto_data.db")
