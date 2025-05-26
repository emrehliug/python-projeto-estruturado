from typing import List
import pandas as pd

""" 
    Transoformar a lista de DataFrame em um unico dataframe_summary_
"""

def transform_data(df: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Transorm all dataframes in a consolidated dataframe.
        pd.DataFrame: Consolidated DataFrame.
    """
    if not df:
        return pd.DataFrame()

    # Concatenate all DataFrames in the list into a single DataFrame
    consolidated_df = pd.concat(df, ignore_index=True)

    # Reset index to ensure it is sequential
    consolidated_df.reset_index(drop=True, inplace=True)

    return consolidated_df