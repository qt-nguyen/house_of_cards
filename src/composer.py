import numpy as np
import pandas as pd
from functools import reduce

DEFAULT_VALUE_MAP = {
    "Yea": 1,
    "Yes": 1,
    "Aye": 1,
    "Nay": -1,
    "No": -1,
    "Present": 0,
    "Not Voting": 0,
    None: 0,          # optional, if using None for missing
    np.nan: 0         # optional, for NaNs
}

class Composer:
    @staticmethod
    def map_values(df: pd.DataFrame,
                   value_map=DEFAULT_VALUE_MAP):
        return df.replace(value_map)
    
    
    @staticmethod
    def filter_excessive_abstentions(df:pd.DataFrame,
                                     threshold=0.2):
        vote_cols = df.columns.difference(['id'], sort=False)
        zero_count = (df[vote_cols] == 0).sum(axis=1)
        zero_ratio = zero_count / len(vote_cols)
        return df[zero_ratio < threshold]
    
    
    @staticmethod
    def normalize_votes(df: pd.DataFrame):
        vote_cols = df.columns.difference(["id"], sort=False)
        df_centered = df.copy()
        df_centered[vote_cols] = df[vote_cols] - df[vote_cols].mean(axis=0)
        return df_centered
        
    
    @staticmethod
    def create_voting_matrix(
        df: pd.DataFrame
    ):
        vote_cols = df.columns.difference(["id"], sort=False)
        return df[vote_cols].values.tolist()
    

    
    

    
    