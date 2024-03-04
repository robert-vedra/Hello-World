import pandas as pd

def clean_dataframe(df):
    """
    Purpose: Remove rows of data that contains 0 data points
    Input: Dataframe with 'unclean' data
    Output: 'Clean' dataframe
    """
    cleandf = df[(df['SR Num_Data_pts'].astype(float) > 0) & (df['FF data_points'].astype(float)>0)]
    return cleandf

