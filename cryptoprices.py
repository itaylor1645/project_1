"""Helper module to get DataFrames for cryptocurrency price data."""

import pandas as pd


def get_btc_prices_df():
    """Get a DataFrame of Bitcoin prices."""
    return pd.read_csv("Resources/BTC_Prices.csv", parse_dates=["Date"])


def get_btc_prices_by_date_df():
    """Get a DataFrame of Bitcoin prices with date as index."""
    return get_btc_prices_df().set_index("Date")


def get_eth_prices_df():
    """Get a DataFrame of Ethereum prices."""
    df = pd.read_csv(
        "Resources/Ethereum Historical Data .csv", parse_dates=["Date"], thousands=","
    ).sort_values("Date")
    # format volume & change percent to be parsed as floats
    df["Vol."] = (
        df["Vol."]
        .replace({"K": "e+03", "M": "e+06", "B": "e+09"}, regex=True)
        .astype(float)
    )
    df["Change %"] = df["Change %"].str.rstrip("%").astype(float) / 100.0
    return df


def get_eth_prices_by_date_df():
    """Get a DataFrame of Ethereum prices with date as index."""
    return get_eth_prices_df().set_index("Date")
