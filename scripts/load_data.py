import pandas as pd

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path: str, delimiter: str = ',') -> pd.DataFrame:
    """
    Load data from a CSV file into a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.
        delimiter (str): The delimiter used in the txt file. Default is ','.

    Returns:
        pd.DataFrame: The loaded data as a pandas DataFrame.
    """
    try:
        logging.info(f"Loading data from {file_path} with delimiter '{delimiter}'")
        df = pd.read_csv(file_path, delimiter=delimiter)
        logging.info("Data loaded successfully")
        return df
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise