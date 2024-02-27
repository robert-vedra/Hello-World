import pandas as pd

def clean_dataframe(df):
    df = pd.read_csv('FF_SR_ data.csv')
    newdf = df[(df['SR Num_Data_pts'].astype(float) > 1) & (df['FF data_points'].astype(float) > 1)]
    return newdf
