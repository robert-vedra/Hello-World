import pandas as pd

def clean_dataframe(df):
    cleandf = df[(df['SR Num_Data_pts'].astype(float) > 0) & (df['FF data_points'].astype(float)>0)]
    return cleandf

