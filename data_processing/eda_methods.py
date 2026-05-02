import pandas as pd
import numpy as np
import scipy.stats as stats
from data_processing.data_processor import DataProcessor

class EDA(DataProcessor):    
     def __init__(self,df:pd.DataFrame, **kwargs):
            super().__init__(df=df)
            self.config=kwargs
            
    
     def col_wise_mean(self) : 
         numeric_df=self.df.select_dtypes(include=[np.number])    
         col_to_mean=numeric_df.mean().to_dict()
         return col_to_mean


        
     def na_values_in_each(self):
         numeric_df=self.df.select_dtypes(include=[np.number])
         null_counts=numeric_df.isnull().sum().to_dict()
         return null_counts 
     

     def mean_abs_deviation(self, col_name: str)->float:
         """Returns the mean absolute deviation of the 
            column/feature name given """
         if not pd.api.types.is_numeric_dtype(self.df[col_name]):
          raise TypeError(f"Column '{col_name}' must be numeric, not {self.df[col_name].dtype}")   
            
         mu= self.__mean__(col_name)
         num=(self.df[col_name]-mu).abs().sum()
         deno=self.df[col_name].count()
         mad=num/deno
         return round(mad,4)
     



