# Unit Test Documentation

This directory contains unit tests for the main scripts in the Insurance Risk Analysis project. Each test file targets a specific module and ensures its core functionalities work as expected.

---

## test_load_data.py

**Purpose:**  
Tests the data loading functions in `scripts/load_data.py`.

**What is tested:**
- Loading a CSV file successfully.
- Handling non-existent CSV files.
- Loading data from a SQLite database table, including datetime conversion.
- Handling non-existent tables in the SQLite database.

**How it works:**  
Temporary files are created for each test and removed after. The tests check for correct DataFrame shapes, types, and error handling.

---

## test_aggregate_data.py

**Purpose:**  
Tests the monthly aggregation logic in `scripts/aggregate_data.py`.

**What is tested:**
- That `compute_monthly_aggregates` correctly groups by month and applies aggregation functions.
- The output DataFrame has the expected columns and values.

**How it works:**  
A sample DataFrame is aggregated, and the results are checked for correctness.

---

## test_plot_generator.py

**Purpose:**  
Tests the plotting methods in `scripts/plot_generator.py`.

**What is tested:**
- That each plotting method can be called without error.
- That each plotting method attempts to display a plot (using `matplotlib.pyplot.show`).

**How it works:**  
The tests use `unittest.mock.patch` to mock `matplotlib.pyplot.show`, ensuring that plots are not actually rendered (which is important for headless test environments). The tests verify that `show()` is called, indicating the plot function executed as expected.

---

**How to run all tests:**

From the project root, run:
```bash
python -m unittest discover tests
```

Or use the VS Code Test Explorer for a graphical interface.

---