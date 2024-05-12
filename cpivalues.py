"""Helper module to get DataFrames for Consumer Price Index data."""

import pandas as pd


def get_cpi_df():
    """Get a DataFrame of CPI."""
    pivot_df = pd.read_csv(
        "Resources/CPI_SeriesReport-20240506224144_c4a067_csv.csv", header=11
    )
    # source is formatted as pivot table of months; melt and format for monthly period
    df = pd.melt(
        pivot_df,
        id_vars="Year",
        value_vars=[
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
        var_name="Month",
        value_name="Value",
    )
    df["Date"] = pd.to_datetime(
        df["Year"].astype(str) + "-" + df["Month"], format="%Y-%b"
    )
    return df.drop(columns=["Year", "Month"]).sort_values("Date").dropna()


def get_cpi_by_date_df():
    """Get a DataFrame of CPI with date as index."""
    return get_cpi_df().set_index("Date")
