import pandas as pd
from data_processing.eda_methods import EDA


class CLEANING(EDA):
    def __init__(self, df: pd.DataFrame, **kwargs):
        super().__init__(df, **kwargs)

    def run(self) -> pd.DataFrame:
        return self.df

    def _validate_column(self, col_name: str) -> None:
        if col_name not in self.df.columns:
            raise KeyError(f"Column '{col_name}' does not exist.")

    def _clean_col_by_mean(self, col_name: str) -> pd.DataFrame:
        self._validate_column(col_name)
        if not pd.api.types.is_numeric_dtype(self.df[col_name]):
            raise TypeError(f"Column '{col_name}' must be numeric for mean cleaning.")

        self.df[col_name] = self.df[col_name].fillna(self.df[col_name].mean())
        return self.df

    def _clean_col_by_mode(self, col_name: str) -> pd.DataFrame:
        self._validate_column(col_name)
        mode_values = self.df[col_name].mode(dropna=True)
        if not mode_values.empty:
            self.df[col_name] = self.df[col_name].fillna(mode_values.iloc[0])
        return self.df

    def _clean_col_by_median(self, col_name: str) -> pd.DataFrame:
        self._validate_column(col_name)
        if not pd.api.types.is_numeric_dtype(self.df[col_name]):
            raise TypeError(f"Column '{col_name}' must be numeric for median cleaning.")

        self.df[col_name] = self.df[col_name].fillna(self.df[col_name].median())
        return self.df

    def clean_col_by(self, col: str, **kwargs) -> pd.DataFrame:
        """Clean one column using mean, mode, or median."""
        methods = {
            "mean": self._clean_col_by_mean,
            "mode": self._clean_col_by_mode,
            "median": self._clean_col_by_median,
        }

        for key, value in kwargs.items():
            if key in methods and value is True:
                return methods[key](col)

        return self.df


Cleaning = CLEANING
