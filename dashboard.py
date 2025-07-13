"""
Streamlit dash.  Run: `streamlit run dashboard.py`
"""
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from config import DATABASE_URL

st.set_page_config(page_title="🪙 Crypto Pulse", layout="wide")

engine = create_engine(DATABASE_URL)
df = pd.read_sql("SELECT * FROM crypto_prices ORDER BY FETCHED_AT DESC", engine)

st.title("🪙 Crypto Pulse – Live Market Snapshot")

# latest pull only
latest = df.groupby("ID").first().reset_index()

st.dataframe(latest[["NAME", "SYMBOL", "CURRENT_PRICE", "MARKET_CAP",
                     "TOTAL_VOLUME", "PRICE_CHANGE_PERCENTAGE_24H"]],
             use_container_width=True)

st.markdown("---")

# price trend of a selected coin
coin = st.selectbox("Select a coin to view price history", latest["NAME"])
hist = df[df["NAME"] == coin].sort_values("FETCHED_AT")

st.line_chart(hist.set_index("FETCHED_AT")["CURRENT_PRICE"], height=350)
