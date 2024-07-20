import os

import pandas as pd


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

def get_data():
    data_dir = os.path.join(SCRIPT_DIR, "../data")
    dfs = {}
    csv_files = [f for f in os.listdir(data_dir) if f.endswith(".csv")]
    for csv_file in csv_files:
        symbol = csv_file.split(".")[0]
        dfs[symbol] = pd.read_csv(os.path.join(data_dir, csv_file))
        # Make sure the "Date" column is a datetime object
        dfs[symbol]["Date"] = pd.to_datetime(dfs[symbol]["Date"])
    return dfs


def make_plot(symbol, data):
    # limit data to the last 100 days
    data = data.tail(100)
    plot_file_name = os.path.join(SCRIPT_DIR, "../images", f"{symbol}.png")
    data.plot(y=["Close"], x="Date").get_figure().savefig(plot_file_name)


def main():
    data = get_data()
    for symbol, df in data.items():
        make_plot(symbol, df)


if __name__ == "__main__":
    main()
