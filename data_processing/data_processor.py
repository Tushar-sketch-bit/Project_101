from abc import ABC, abstractmethod
import pandas as pd


class DataProcessor(ABC):
    def __init__(self, df: pd.DataFrame):
        self.df = df

    @abstractmethod
    def run(self):
        """Every child must implement a run method."""
        pass

    def save_state(self, filename: str) -> None:
        """Save the current dataframe state to a CSV file."""
        self.df.to_csv(filename, index=False)
        print(f"Progress saved to {filename}")

    @staticmethod
    def user_params(params: dict) -> list:
        unique_values = []
        for value in params.values():
            if value not in unique_values:
                unique_values.append(value)
        return unique_values
