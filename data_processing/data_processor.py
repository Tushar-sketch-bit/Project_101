from abc import ABC, abstractmethod
import pandas as pd

class DataProcessor(ABC):
    def __init__(self, df: pd.DataFrame):
        self.df = df

    @abstractmethod
    def run(self):
        """Every child must implement a run method."""
        pass

    @abstractmethod    
    def save_state(self, filename):
        """Common logic shared by all processors."""
        self.df.to_csv(filename)
        print(f"Progress saved to {filename}")


    def user_params(dict:dict)->list:
        List=[]
        for key, value in dict:
          if List.__contains__(value):
            pass
          else:
            List.append(value)
        
        return List

