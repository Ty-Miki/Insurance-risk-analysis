import unittest
import os
import pandas as pd
import sqlite3
from scripts import load_data

class TestLoadData(unittest.TestCase):
    def setUp(self):
        # Create a sample CSV file
        self.csv_path = "test_sample.csv"
        pd.DataFrame({"A": [1, 2], "B": [3, 4]}).to_csv(self.csv_path, index=False)
        # Create a sample SQLite DB
        self.db_path = "test_sample.db"
        conn = sqlite3.connect(self.db_path)
        pd.DataFrame({"id": [1, 2], "date": ["2020-01-01", "2020-02-01"]}).to_sql("test_table", conn, index=False, if_exists="replace")
        conn.close()

    def tearDown(self):
        os.remove(self.csv_path)
        os.remove(self.db_path)

    def test_load_data_success(self):
        df = load_data.load_data(self.csv_path, ",")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (2, 2))

    def test_load_data_file_not_exist(self):
        df = load_data.load_data("nonexistent.csv", ",")
        self.assertIsNone(df)

    def test_load_from_sqlite_success(self):
        df = load_data.load_from_sqlite(self.db_path, "test_table", datetime_cols=["date"])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (2, 2))
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(df["date"]))

    def test_load_from_sqlite_table_not_exist(self):
        df = load_data.load_from_sqlite(self.db_path, "no_table")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(df.empty)