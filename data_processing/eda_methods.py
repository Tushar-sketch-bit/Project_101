import pandas as pd
import numpy as np
from data_processing.data_processor import DataProcessor


class EDA(DataProcessor):
    def __init__(self, df: pd.DataFrame, **kwargs):
        super().__init__(df=df)
        self.config = kwargs

    @property
    def numeric_df(self) -> pd.DataFrame:
        return self.df.select_dtypes(include=[np.number])

    def run(self) -> dict:
        """Return a compact EDA report for prompt building and UI display."""
        numeric_df = self.numeric_df
        report = {
            "shape": {"rows": len(self.df), "columns": len(self.df.columns)},
            "columns": self.df.columns.tolist(),
            "numeric_columns": numeric_df.columns.tolist(),
            "missing_values": self.na_values_in_each(),
            "means": self.col_wise_mean(),
        }

        if not numeric_df.empty:
            report["describe"] = numeric_df.describe().round(4).to_dict()
            report["correlations"] = numeric_df.corr(numeric_only=True).round(4).to_dict()
        else:
            report["describe"] = {}
            report["correlations"] = {}

        return report

    def col_wise_mean(self) -> dict:
        return self.numeric_df.mean().round(4).to_dict()

    def na_values_in_each(self) -> dict:
        return self.df.isnull().sum().to_dict()

    def mean_abs_deviation(self, col_name: str) -> float:
        """Return the mean absolute deviation for a numeric column."""
        if col_name not in self.df.columns:
            raise KeyError(f"Column '{col_name}' does not exist.")

        if not pd.api.types.is_numeric_dtype(self.df[col_name]):
            raise TypeError(f"Column '{col_name}' must be numeric, not {self.df[col_name].dtype}")

        mean_value = self.df[col_name].mean()
        mad = (self.df[col_name] - mean_value).abs().mean()
        return round(float(mad), 4)
