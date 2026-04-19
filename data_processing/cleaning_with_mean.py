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
         
         prop_float:float = proportion / 100
         if pd.api.types.is_numeric_dtype(self.df[col_name]):
             
          stats.trim_mean(self.df[col_name],prop_float)
     
     
     
    def clean_whole_data_by(self,**kwargs):
        """_summary_
        """
        methods = {
        'mean': self._clean_whole_data_by_mean,
        'mode': self._clean_whole_data_by_mode,
        'trim': self._trimmean_for # Assuming you adapt this for the whole df
          }

        for key, value in kwargs.items():
         if key in methods and value is True:
            return methods[key]()
            
        return self.df