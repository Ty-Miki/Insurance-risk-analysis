import unittest
import pandas as pd
from scripts import aggregate_data

class TestAggregateData(unittest.TestCase):
    def test_compute_monthly_aggregates(self):
        df = pd.DataFrame({
            "TransactionMonth": ["2023-01-15", "2023-01-20", "2023-02-10"],
            "TotalClaims": [10, 20, 30],
            "TotalPremium": [100, 200, 300]
        })
        agg_config = {"TotalClaims": "sum", "TotalPremium": "mean"}
        result = aggregate_data.compute_monthly_aggregates(df, "TransactionMonth", agg_config)
        self.assertEqual(result.shape[0], 2)
        self.assertIn("Month", result.columns)
        self.assertEqual(result.loc[0, "TotalClaims"], 30)
        self.assertAlmostEqual(result.loc[0, "TotalPremium"], 150)