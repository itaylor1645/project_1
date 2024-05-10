"""Helper module to get DataFrames for metal futures data.

All metal futures data should have common column names:
* date
* open
* high
* low
* close
* volume
"""

import pandas as pd


def _read_metal_futures_df(filepath):
    """Helper method to read CSV of metal futures to DataFrame."""
    return pd.read_csv(filepath, parse_dates=["date"])


def get_gold_futures_df():
    """Get a DataFrame of Gold Futures."""
    return _read_metal_futures_df("Resources/Gold_Futures.csv")


def get_silver_futures_df():
    """Get a DataFrame of Silver Futures."""
    return _read_metal_futures_df("Resources/Silver_Futures.csv")
