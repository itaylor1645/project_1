"""Helper module to get DataFrames for federal interest rate data."""

import pandas as pd


def get_fed_interest_rate_df():
    """Get a DataFrame of federal interest rates."""
    return pd.read_csv(
        "Resources/FEDFUNDS (interest rate 2014).csv", parse_dates=["DATE"]
    )


def get_fed_interest_rate_by_date_df():
    """Get a DataFrame of federal interest rates with date as index."""
    return get_fed_interest_rate_df().set_index("DATE")
