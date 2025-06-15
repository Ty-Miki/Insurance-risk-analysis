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

    def plot_grouped_bar_chart(
        self, 
        df: pd.DataFrame, 
        column: str, 
        group_by: Union[str, List[str]], 
        agg_func: str = "mean"
    ):
        """
        Generates grouped bar charts for a numerical column after grouping by one or more categorical columns.

        Parameters:
            df (pd.DataFrame): The input DataFrame containing the data.
            value_col (str): The numeric column to aggregate and plot.
            group_cols (Union[str, List[str]]): One or more categorical columns to group by.
            agg_func (str): Aggregation function to apply ('mean', 'sum', etc.). Default is 'mean'.
        """
        group_by = [group_by] if isinstance(group_by, str) else group_by
        try:
            grouped = df.groupby(group_by)[column].agg(agg_func).reset_index()

            if len(group_by) == 1:
                # Simple bar plot
                sns.barplot(data=grouped, x=group_by[0], y=column)
            else:
                # Grouped bar plot with hue
                sns.barplot(data=grouped, x=group_by[0], y=column, hue=group_by[1])

            plt.title(f'{agg_func.capitalize()} of {column} grouped by {" and ".join(group_by)}')
            plt.xlabel(group_by[0])
            plt.ylabel(f'{agg_func.capitalize()} of {column}')
            plt.xticks(rotation=45)
            logging.info(f"Grouped bar chart for {column} by {group_by} created successfully.")
            plt.tight_layout()
            plt.show()

        except Exception as e:
            logging.error(f"Error generating grouped bar chart for {column} by {group_by}: {e}")
