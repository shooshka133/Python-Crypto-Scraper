# 📊 CoinGecko Crypto Price Scraper

A simple Python script to fetch and log the top 10 cryptocurrencies from the CoinGecko API. Saves data to a CSV with price, name, 24h change, and timestamp.

## 🛠 Features

- Top 10 coins by market cap
- CSV export with timestamp
- Supports periodic fetching (e.g., every 60s)
- Logging to `scraper.log`
- Command-line support with `--runs` flag

## 🚀 Setup

```bash
git https://github.com/shooshka133/Python-Crypto-Scraper.git
cd CryptoScraper
pip install -r requirements.txt
python scraper.py --runs 3
