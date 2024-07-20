import os
import tomllib

import yfinance as yf


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def get_symbols():
    with open(os.path.join(SCRIPT_DIR, "../config/config.toml"), "rb") as f:
        config = tomllib.load(f)
    return config["symbols"]


def download_data(symbol):
    history = yf.Ticker(symbol).history(period="max")
    file_name = os.path.join(SCRIPT_DIR, "../data", f"{symbol}.csv")
    history.to_csv(file_name)


def main():
    symbols = get_symbols()
    for symbol in symbols:
        download_data(symbol)


if __name__ == "__main__":
    main()
