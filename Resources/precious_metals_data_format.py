"""Format raw downloaded gold/silver futures files for analysis.

Raw files are expected to be downloaded from `precious_metals_data_dl.py` and
located in `./precious-metals-data/`.
"""

import pandas as pd

if __name__ == "__main__":

    def read_csv(filepath: str, start_date: str, end_date: str):
        """Read in CSV as DataFrame, formatting before return.

        The return is sorted by ascending date and filtered for missing values & a date range.
        """
        df = pd.read_csv(filepath, parse_dates=["date"]).dropna().sort_values("date")
        return df.loc[(df["date"] >= start_date) & (df["date"] <= end_date)]

    def to_csv(df: pd.DataFrame, filepath: str):
        """Save DataFrame to a CSV."""
        df.to_csv(filepath, index=False)

    start_date = "2015-01-01"
    end_date = "2024-04-01"

    # read from folder holding downloads, then save with descriptive filename
    gold_df = read_csv(
        "precious-metals-data/individual_data/Gold_data.csv", start_date, end_date
    )
    to_csv(gold_df, "Gold_Futures.csv")

    silver_df = read_csv(
        "precious-metals-data/individual_data/Silver_data.csv", start_date, end_date
    )
    to_csv(silver_df, "Silver_Futures.csv")
