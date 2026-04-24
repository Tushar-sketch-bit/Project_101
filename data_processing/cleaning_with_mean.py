import pandas as pd
import numpy as np
import scipy.stats as stats

class CLEANING: 
    def __init__(self, df: pd.DataFrame, **kwargs):
        self.df = df
        self.config = kwargs
        
    def _clean_whole_data_by_mean(self):
        try:
         self.df= self.df.apply((lambda x: x.fillna(x.mean()) 
                               if pd.api.types.is_numeric_dtype(x) 
                               else x.fillna(x.mode()[0])))
        except Exception:
           print("there was an error cleaning data")  
           return self.df
       
    def _clean_whole_data_by_mode(self):
        try:
         self.df= self.df.apply((lambda x: x.fillna(x.mode()[0]) 
                               if pd.api.types.is_numeric_dtype(x) 
                               else x.fillna(x.mode()[0])))
        except Exception:
           print("there was an error cleaning data")  
           return self.df
     
    def _trimmean_for(self,col_name:str, proportion:int=10):
         """Helps in calculating the trimmean for the specific column given 

         Args:
             col_name (str): Name of the column for which you 
                             need to calculate the trim mean
             proportion: default proportion cut is 0.1 i.e 10% from both ends 
         """
         try: 
          prop_float:float = proportion / 100
          if pd.api.types.is_numeric_dtype(self.df[col_name]):  
           stats.trim_mean(self.df[col_name],prop_float)
         except Exception:
             print("Could not calculate trim mean ")
     
    def _clean_data_by_median(self, col_name:str): 
            """_summary_
    
            Args:
                col_name (str): _description_
            """
            try:
              if pd.api.types.is_numeric_dtype(self.df[col_name]):
                median_value = self.df[col_name].median()
                self.df[col_name] = self.df[col_name].fillna(median_value)
            except Exception:
                print("Could not clean data by median")
     
    def clean_whole_data_by(self,**kwargs):
        """Replace NULL values in the whole data by specified method in the kwargs. 
           You can specify one method at a time. If you specify more than one method, 
           it will return the data without cleaning.
           
           kwargs: {methods: mean/ mode/ median}
        """
        methods = {
        'mean': self._clean_whole_data_by_mean,
        'mode': self._clean_whole_data_by_mode, 
        'median': self._clean_data_by_median
          }

        for key, value in kwargs.items():
         if key in methods and value is True:
            return methods[key]()
            
        return self.df
    
    
    def basic_stats_for_col(self, col_name:str):
        """_summary_

        Args:
            col_name (str): _description_

        Returns:
            _type_: _description_
        """
        try:
         if pd.api.types.is_numeric_dtype(self.df[col_name]):
            mean_value = self.df[col_name].mean()
            median_value = self.df[col_name].median()
            mode_value = self.df[col_name].mode()[0]
            std_dev = self.df[col_name].std()
            stats={
                f'mean of {col_name}': mean_value,
                f'median of {col_name}': median_value,
                f'mode of {col_name}': mode_value,
                f'std_dev of {col_name}': std_dev
            }
            return stats
        except Exception:
            print(f"Error occurred while calculating basic statistics for column '{col_name}'.")