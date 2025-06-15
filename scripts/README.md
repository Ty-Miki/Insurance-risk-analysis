# Insurance Risk Analysis Scripts Documentation

## 1. Data Loading (`load_data.py`)

This module provides functions to load data from CSV files and SQLite databases.

- **`load_data(filepath, delimiter)`**  
  Loads a CSV file into a pandas DataFrame.  
  - Returns `None` if the file does not exist or loading fails.
  - Logs success or failure.

- **`load_from_sqlite(db_path, table_name, datetime_cols=None)`**  
  Loads a table from a SQLite database into a DataFrame.  
  - Optionally converts specified columns to datetime.
  - Returns an empty DataFrame on failure.

---

## 2. Plot Generation (`plot_generator.py`)

The `PlotGenerator` class provides methods for generating various plots for exploratory data analysis:

- **`plot_histogram(df, columns, bins=30)`**  
  Plots histograms (with KDE) for specified columns.

- **`plot_bar_chart(df, columns)`**  
  Plots bar charts for categorical columns.

- **`plot_grouped_bar_chart(df, column, group_by, agg_func='mean')`**  
  Plots grouped bar charts for a numeric column grouped by one or more categorical columns.

- **`plot_monthly_trends(df, date_col, agg_config, title_map=None)`**  
  Plots monthly trends for specified aggregations.

- **`plot_horizontal_bar(df, title, x_col, y_col)`**  
  Plots horizontal bar charts.

- **`plot_correlation_matrix(df)`**  
  Plots a heatmap of the correlation matrix for numeric columns.

- **`plot_scatter_by_category(df, numeric_cols, categorical_cols)`**  
  Plots scatter (strip) plots of numeric columns against categorical columns.

---

## 3. Data Aggregation (`aggregate_data.py`)

- **`compute_monthly_aggregates(df, date_col, agg_config)`**  
  Groups the DataFrame by month (using a datetime column) and aggregates specified columns using provided aggregation functions.  
  - Returns a DataFrame with a "Month" column and aggregated values.

---