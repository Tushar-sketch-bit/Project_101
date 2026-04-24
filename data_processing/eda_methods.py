import pandas as pd
import numpy as np
import scipy.stats as stats
class EDA:
    
     def __init__(self,df:pd.DataFrame, **kwargs):
            self.df=df
            self.config=kwargs
            
    
     def col_wise_mean(self,COLS:list=[]) : 
        for col_names in COLS:
            if pd.api.types.is_numeric_dtype(self.df[col_names]):
                print(f'{col_names} mean: {self.df[col_names].mean()}')
        return self     
    
     def mean_for(self, col_name:str):
         if pd.api.types.is_numeric_dtype(self.df[col_name]):
             print(f'{col_name} mean: {self.df[col_name].mean()}')
         else:
             print(f"Column '{col_name}' is not numeric.")
         return self
     
     def trimmean_for(self,col_name:str, proportion:int=10):
         """Helps in calculating the trimmean for the specific column given 

         Args:
             col_name (str): Name of the column for which you 
                             need to calculate the trim mean
             proportion: default proportion cut is 0.1 i.e 10% from both ends 
         """
         
         prop_float:float = proportion / 100
         if pd.api.types.is_numeric_dtype(self.df[col_name]):
             
          stats.trim_mean(self.df[col_name],prop_float)
         else:
            print(f"Column '{col_name}' is not numeric.")
                
     def na_values_in_each(self, COLS:list=[]):
         numeric_df=self.df.select_dtypes(include=[np.number])
         null_counts=numeric_df.isnull().sum()
         for col, count in null_counts.items():
            print(f"Column '{col}' has {count} NaN values")
         
         return self   
     
       
     def multiply_two_features(self, col1:str, col2:str, new_col:str):
          self.df[new_col]=self.df[col1]*self.df[col2]
          return self
      
     def add_two_features(self, col1:str, col2:str, new_col:str):
          self.df[new_col]=self.df[col1]+self.df[col2]
          return self
      
       
     
     def df_metadata(self):
         print("DataFrame Info:")
         
         print(self.df.info())
        
         print(f"\nkeyword args given: {self.config}")
         return self
     
     def __mean__(self, col_name):  
         return self.df[col_name].mean()
     
     
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