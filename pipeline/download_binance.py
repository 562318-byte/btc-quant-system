import requests
import pandas as pd
import time
import os

BASE_URL = "https://api.binance.com/api/v3/klines"

def download_btc(symbol="BTCUSDT", interval="1h", limit=1000):
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    r = requests.get(BASE_URL, params=params)
    r.raise_for_status()
    data = r.json()

    df = pd.DataFrame(data, columns=[
        "open_time","open","high","low","close","volume",
        "close_time","quote_asset_volume","number_of_trades",
        "taker_buy_volume","taker_buy_quote","ignore"
    ])

    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
    df["close_time"] = pd.to_datetime(df["close_time"], unit="ms")

    numeric_cols = ["open","high","low","close","volume"]
    df[numeric_cols] = df[numeric_cols].astype(float)

    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/btc_1h.csv", index=False)

    return df


if __name__ == "__main__":
    df = download_btc()
    print(df.head())
