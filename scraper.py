import requests
import pandas as pd
from datetime import datetime
import time
import logging
import argparse

def scrape_coingecko_api(runs=1, interval=60):
    """
    Fetches top 10 cryptocurrencies from CoinGecko API and saves to CSV.
    Args:
        runs (int): Number of fetches (default: 1).
        interval (int): Seconds between fetches (default: 60).
    Returns:
        int: Total number of coins fetched across all runs.
    """
    # Set up logging
    logging.basicConfig(filename='scraper.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1"
    headers = {"accept": "application/json", "User-Agent": "Mozilla/5.0"}
    total_coins = 0

    for run in range(runs):
        try:
            run_start_time = time.time()  # Renamed to avoid shadowing
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()

            # Format data for DataFrame
            coins = [
                {
                    "Coin Name": coin["name"],
                    "Price": coin["current_price"],
                    "Change_24h": coin["price_change_percentage_24h"],
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                for coin in data
            ]

            # Save to CSV (append mode for multiple runs)
            df = pd.DataFrame(coins)
            mode = 'a' if run > 0 else 'w'
            df.to_csv("crypto_prices.csv", mode=mode, index=False, header=(run == 0))

            total_coins += len(coins)
            logging.info(f"Run {run + 1}: Fetched {len(coins)} coins, saved to crypto_prices.csv")
            print(f"Run {run + 1}: Fetched {len(coins)} coins in {time.time() - run_start_time:.2f} seconds")

            if run < runs - 1:
                time.sleep(interval)

        except requests.exceptions.RequestException as e:
            logging.error(f"Network error: {e}")
            print(f"Error: {e}")
        except ValueError as e:
            logging.error(f"JSON parsing error: {e}")
            print(f"Error: JSON parsing failed")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            print(f"Error: {e}")

    return total_coins  # Moved outside try/loop for explicit return


# if __name__ == "__main__":
#     start_time = time.time()
#     total_fetched = scrape_coingecko_api(runs=3, interval=60)  # Fetch 3 times, 60s apart
#     print(f"Total coins fetched: {total_fetched} in {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CoinGecko API Scraper")
    parser.add_argument('--runs', type=int, default=3, help='Number of fetches')
    args = parser.parse_args()
    start_time = time.time()
    total_fetched = scrape_coingecko_api(runs=args.runs, interval=60)
    print(f"Total coins fetched: {total_fetched} in {time.time() - start_time:.2f} seconds")
