title: "Crypto Pulse — Real-Time Crypto Tracker with API Pipeline & Dashboard"
description: >
  Crypto Pulse is an end-to-end data pipeline project that:
  - Fetches live cryptocurrency prices from the CoinGecko API
  - Cleans and processes the data using Pandas
  - Stores it in a local SQLite database
  - Displays a real-time dashboard using Streamlit
  This project showcases practical skills in API integration, data engineering, and dashboarding — perfect for portfolios and interview prep.

features:
  - "🔄 Live data fetch from CoinGecko API (top 50 coins by market cap)"
  - "🧪 Cleans and enriches data (adds timestamp, enforces types)"
  - "🧱 Stores data in SQLite (easily switchable to PostgreSQL)"
  - "📈 Interactive dashboard with real-time graphs & filters"
  - "⏱️ Supports automation with cron jobs or Windows Task Scheduler"

tech_stack:
  - Python 3.8+
  - pandas
  - requests
  - sqlalchemy
  - streamlit
  - CoinGecko API

project_structure:
  - fetch_data.py: "Pulls live crypto data"
  - db_store.py: "Stores data into the database"
  - dashboard.py: "Streamlit dashboard"
  - config.py: "API and DB config"
  - requirements.txt: "Project dependencies"
  - .env: "Optional DB URL override"
  - README.md: "You're here"

setup:
  prerequisites:
    - "Python 3.8+"
    - "Git installed"
    - "Internet connection"
  installation_windows:
    - "git clone https://github.com/<your-username>/crypto-pulse.git"
    - "cd crypto-pulse"
    - "python -m venv venv"
    - "venv\\Scripts\\activate"
    - "pip install -r requirements.txt"
    - "python db_store.py"
    - "streamlit run dashboard.py"

automation:
  windows_task_scheduler:
    - "Open Task Scheduler"
    - "Create new basic task → Choose 'Daily' or 'Every 30 minutes'"
    - "Set Action: Run program"
    - "Program/script: python C:\\full\\path\\to\\crypto-pulse\\db_store.py"

like_this_project: "Drop a ⭐️ on GitHub if you found it helpful, or fork it and make it even better!"
