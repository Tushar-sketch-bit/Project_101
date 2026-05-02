import pandas as pd
import numpy as np
import scipy.stats as stats
from eda_methods import EDA




class CLEANING(EDA):
    
 COL_GIVEN:str=None

 def __init__(self, df: pd.DataFrame, **kwargs):
      super().__init__(df,**kwargs)
        
 def _clean_col_by_mean(self,col_name=COL_GIVEN):
        try:
         if pd.api.types.is_numeric_dtype(self.df[col_name]):
          self.df[col_name].fillna(self.df[col_name].mean())
          return self.df
        except Exception:
           print("there was an error cleaning data")  
       
 def _clean_col_by_mode(self,col_name=COL_GIVEN):
        try:
         if pd.api.types.is_numeric_dtype(self.df[col_name]):
           self.df[col_name].fillna(self.df[col_name].mode())
         return self.df
        except Exception:
           print("there was an error cleaning data")  


 def _clean_col_by_median(self,col_name=COL_GIVEN):
    try:
        if pd.api.types.is_numeric_dtype(self.df[col_name]):
         self.df[col_name].fillna(self.df[col_name].median())
        return self.df
    except Exception:
        print("error in cleaning data")
    
 def clean_col_by(self, col,**kwargs):
        """A parent method that uses dynamic way to clean whole data
        """

        COL_GIVEN=col
        methods = {
        'mean': self._clean_col_by_mean,
        'mode': self._clean_col_by_mode,
        'median': self._clean_col_by_median 
          }

        for key, value in kwargs.items():
         if key in methods and value is True:
            return methods[key]()
            
        return self.df 