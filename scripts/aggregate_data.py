import pandas as pd
from typing import Dict

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def compute_monthly_aggregates(
    df: pd.DataFrame,
    date_col: str,
    agg_config: Dict[str, str]
) -> pd.DataFrame:
    """
    Groups the DataFrame by month and aggregates columns as specified.

    Parameters:
        df (pd.DataFrame): Input data.
        date_col (str): Name of the datetime column (e.g., 'TransactionMonth').
        agg_config (Dict[str, str]): Dictionary mapping columns to aggregation functions
                                     (e.g., {'TotalClaims': 'sum', 'TotalPremium': 'mean'}).

    Returns:
        pd.DataFrame: Monthly aggregated data with datetime index.
    """
    try:
        df = df.copy()
        df[date_col] = pd.to_datetime(df[date_col])
        df["Month"] = df[date_col].dt.to_period("M")
        grouped = df.groupby("Month").agg(agg_config).reset_index()
        grouped["Month"] = grouped["Month"].dt.to_timestamp()
        logging.info("Monthly aggregation completed successfully.")
        return grouped
    except Exception as e:
        logging.error(f"Error in compute_monthly_aggregates: {e}")
        raise
