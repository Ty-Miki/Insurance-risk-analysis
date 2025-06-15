# Notebook Documentation

This documentation covers the two main notebooks in this project:  
- `data_cleaning.ipynb` (Data Inspection and Cleaning)  
- `EDA.ipynb` (Exploratory Data Analysis)

---

## 1. `data_cleaning.ipynb`: Data Inspection and Cleaning

This notebook demonstrates the **inspection** and **cleaning** of raw insurance claim data in preparation for analysis and modeling.

### **Sections**

#### **Setup and Data Loading**
- Adds the parent directory to `sys.path` for module imports.
- Loads a pipe-delimited (`|`) text file into a pandas DataFrame using `load_data`.

#### **Initial Inspection**
- Checks DataFrame shape and columns.
- Inspects data types and missing values.
- Displays a preview of the data.

#### **Cleaning Steps**
- **Missing Values:**  
  Drops columns with many missing values and rows missing key vehicle info.
- **Imputation:**  
  Fills missing categorical values with the mode or "Unknown". Drops rows with missing `CapitalOutstanding`.
- **Data Type Casting:**  
  Converts date columns to pandas datetime.
- **Normalization:**  
  Standardizes categorical fields (e.g., lowercase, strip whitespace).
- **Saving Cleaned Data:**  
  Saves the cleaned DataFrame to a SQLite database for further analysis.

#### **Summary**
- Provides a systematic approach to data cleaning, ensuring the dataset is ready for EDA and modeling.

---

## 2. `EDA.ipynb`: Exploratory Data Analysis

This notebook performs **exploratory data analysis** on the cleaned insurance claims data.

### **Sections**

#### **Data Loading**
- Loads the cleaned data from the SQLite database using `load_from_sqlite`.
- Ensures date columns are parsed as datetime.
- Displays DataFrame info.

#### **Descriptive Statistics**
- Computes summary statistics for key financial columns (`CalculatedPremiumPerTerm`, `TotalPremium`, `TotalClaims`).
- Checks for negative values in financial columns and logs their counts.
- Provides interpretation and notes on data quality (e.g., negative values, skewness, outliers).

#### **Visualizations**
- **Histograms:**  
  Plots distributions of major numeric columns and vehicle specifications.
- **Bar Charts:**  
  Visualizes categorical distributions (e.g., `Gender`, `Province`, `VehicleType`, `Cylinders`).
- **Loss Ratio Analysis:**  
  Calculates and visualizes loss ratio (`TotalClaims` / `TotalPremium`) by various categories (Province, VehicleType, Gender).
- **Temporal Analysis:**  
  Plots monthly trends for claims count and premium collection using the `plot_monthly_trends` method.

#### **Vehicle Make/Model Claim Distribution**
- Aggregates and sorts average claims by vehicle make and model.
- Displays top and bottom 10 makes/models by average claims.
- Visualizes these using horizontal bar charts.

#### **Correlation and Feature Relationship Mapping**
- **Correlation Matrix:**  
  Plots a heatmap of correlations between numeric features.
- **Scatter/Strip Plots:**  
  Visualizes relationships between numeric and categorical variables.

---

## **How to Use These Notebooks**

1. **Run `data_cleaning.ipynb` first** to clean and save the data.
2. **Run `EDA.ipynb`** to explore the cleaned data, generate statistics, and visualize key patterns and relationships.

---

## **Key Takeaways**

- The workflow ensures data quality and readiness for modeling.
- EDA provides insights into data distribution, anomalies, and relationships, guiding further analysis and feature engineering.

---