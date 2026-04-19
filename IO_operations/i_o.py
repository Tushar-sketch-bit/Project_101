import os
import pandas as pd


class DataLoader:
    @staticmethod
    def load_data(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
    
        try:
            data = pd.read_csv(file_path)
            return data
        except Exception as e:
            print(f"An error occurred while loading the data: {e}")
        return None
    
    @staticmethod
    def close_file(file:pd.DataFrame):
        try:
             del file
        except Exception as e:
            print(f"An error occurred while closing the file: {e}")