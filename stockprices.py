"""Helper module to get DataFrames for stock price data."""

import pandas as pd


def get_nasdaq_df():
    """Get a DataFrame of NASDAQ stock prices."""
    return (
        pd.read_csv(
            "Resources/NASDAQ_Comp_HistoricalData_1715050466921.csv",
            parse_dates=["Date"],
        )
        .dropna()
        .sort_values("Date")
    )


def get_nasdaq_by_date_df():
    """Get a DataFrame of NASDAQ stock prices with date as index."""
    return get_nasdaq_df().set_index("Date")


def get_sp500_df():
    """Get a DataFrame of S&P 500 stock prices."""
    return (
        pd.read_csv(
            "Resources/SP500_HistoricalData_1715050201148.csv", parse_dates=["Date"]
        )
        .dropna()
        .sort_values("Date")
    )


def get_sp500_by_date_df():
    """Get a DataFrame of S&P 500 stock prices with date as index."""
    return get_sp500_df().set_index("Date")
