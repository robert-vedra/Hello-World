import pandas as pd

def clean_dataframe(df):
    #newdf = ffsrdata[(ffsrdata['SR Num_Data_pts'] > 0 ) & (['FF Data_pts'] > 0)]
    newdf = df[(df['SR Num_Data_pts'].astype(float) > 0) & (df['FF data_points'].astype(float)>0)]
    return newdf


