# CoinGecko Crypto Price Scraper
Fetches top 10 cryptocurrencies from CoinGecko API, saving name, price, and 24h change to CSV.

## Features
- Fetches 10 coins in ~0.5s per run.
- Supports periodic fetching (e.g., every 60s).
- Logs errors/success to `scraper.log`.
- Command-line argument for run count.

## Setup
```bash
pip install requests pandas
python scraper.py --runs 3