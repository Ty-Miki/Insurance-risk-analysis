import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import logging
from typing import List, Union

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PlotGenerator:
    """
    A utility class to encapsulate plot generation logic for EDA.
    """

    def __init__(self):
        logging.info("PlotGenerator initialized")

    def plot_histogram(self, df: pd.DataFrame, columns: Union[str, List[str]], bins=30):
        """
        Generates histograms (with KDE) for the specified columns in the given DataFrame.
        Parameters:
            df (pd.DataFrame): The input DataFrame containing the data.
            columns (Union[str, List[str]]): Column name or list of column names to plot.
            bins (int, optional): Number of bins for the histogram. Default is 30.
        """
        columns = [columns] if isinstance(columns, str) else columns
        n = len(columns)
        fig, axes = plt.subplots(1, n, figsize=(6 * n, 4))
        axes = axes if isinstance(axes, np.ndarray) else [axes]

        for ax, col in zip(axes, columns):
            try:
                sns.histplot(df[col], bins=bins, kde=True, ax=ax)
                ax.set_title(f'Histogram of {col}')
                ax.set_xlabel(col)
                logging.info(f"Histogram for {col} created successfully.")
            except Exception as e:
                logging.error(f"Error generating histogram for {col}: {e}")
        
        plt.tight_layout()
        plt.show()

    def plot_bar_chart(self, df: pd.DataFrame, columns: Union[str, List[str]]):
        """
        Generates bar charts for the specified categorical columns or value counts in the given DataFrame.
        
        Parameters:
            df (pd.DataFrame): The input DataFrame containing the data.
            columns (Union[str, List[str]]): Column name or list of column names to plot.
        """
        columns = [columns] if isinstance(columns, str) else columns
        n = len(columns)
        fig, axes = plt.subplots(1, n, figsize=(6 * n, 4))
        axes = axes if isinstance(axes, np.ndarray) else [axes]

        for ax, col in zip(axes, columns):
            try:
                value_counts = df[col].value_counts().sort_index()
                sns.barplot(x=value_counts.index, y=value_counts.values, ax=ax)
                ax.set_title(f'Bar Chart of {col}')
                ax.set_xlabel(col)
                ax.set_ylabel('Count')
                ax.tick_params(axis='x', rotation=45)
                logging.info(f"Bar chart for {col} created successfully.")
            except Exception as e:
                logging.error(f"Error generating bar chart for {col}: {e}")
        
        plt.tight_layout()
        plt.show()
