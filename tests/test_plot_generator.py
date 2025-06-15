import unittest
import pandas as pd
from unittest.mock import patch
from scripts.plot_generator import PlotGenerator

class TestPlotGenerator(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            "A": [1, 2, 3, 4, 5],
            "B": [5, 4, 3, 2, 1],
            "C": ["x", "y", "x", "y", "x"],
            "D": pd.date_range("2023-01-01", periods=5, freq="ME")
        })
        self.pg = PlotGenerator()

    @patch("matplotlib.pyplot.show")
    def test_plot_histogram(self, mock_show):
        self.pg.plot_histogram(self.df, "A")
        mock_show.assert_called_once()

    @patch("matplotlib.pyplot.show")
    def test_plot_bar_chart(self, mock_show):
        self.pg.plot_bar_chart(self.df, "C")
        mock_show.assert_called_once()

    @patch("matplotlib.pyplot.show")
    def test_plot_grouped_bar_chart(self, mock_show):
        self.pg.plot_grouped_bar_chart(self.df, "A", "C")
        mock_show.assert_called_once()

    @patch("matplotlib.pyplot.show")
    def test_plot_monthly_trends(self, mock_show):
        agg_config = {"A": "sum"}
        self.pg.plot_monthly_trends(self.df, "D", agg_config)
        mock_show.assert_called_once()

    @patch("matplotlib.pyplot.show")
    def test_plot_horizontal_bar(self, mock_show):
        self.pg.plot_horizontal_bar(self.df, "Test", "A", "C")
        mock_show.assert_called_once()

    @patch("matplotlib.pyplot.show")
    def test_plot_correlation_matrix(self, mock_show):
        self.pg.plot_correlation_matrix(self.df)
        mock_show.assert_called_once()

    @patch("matplotlib.pyplot.show")
    def test_plot_scatter_by_category(self, mock_show):
        self.pg.plot_scatter_by_category(self.df, ["A"], ["C"])
        mock_show.assert_called_once()