import pandas as pd
import logging
import os
import sqlite3

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def load_data(filepath, delimiter):
    """
    Load a CSV file and return a DataFrame.
    
    Args:
        filepath (str): Path to the CSV file.
        delimiter (str): Delimiter used in the file.
    Returns:
        pd.DataFrame or None
    """
    if not os.path.exists(filepath):
        logging.error(f"File does not exist: {filepath}")
        return None

    try:
        df = pd.read_csv(filepath, delimiter=delimiter)
        logging.info(f"Successfully loaded data from {filepath} with shape {df.shape}")
        return df
    except Exception as e:
        logging.exception(f"Failed to load data from {filepath}")
        return None


def load_from_sqlite(db_path: str, table_name: str, datetime_cols: list = None) -> pd.DataFrame:
    """
    Loads a table from a SQLite database into a pandas DataFrame,
    and optionally converts specified columns to datetime.

    Parameters:
    - db_path (str): Path to the SQLite database file.
    - table_name (str): Name of the table to load.
    - datetime_cols (list): List of column names to convert to datetime.

    Returns:
    - pd.DataFrame: Loaded DataFrame.
    """
    try:
        conn = sqlite3.connect(db_path)
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, conn)
        conn.close()

        if datetime_cols:
            for col in datetime_cols:
                df[col] = pd.to_datetime(df[col], errors='coerce')

        logging.info(f"Loaded {len(df)} records from table '{table_name}'.")
        return df
    except Exception as e:
        logging.error(f"Error loading table '{table_name}' from database: {e}")
        return pd.DataFrame()

