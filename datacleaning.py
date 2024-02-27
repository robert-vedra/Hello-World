import pandas as pd

def clean_dataframe(df):

    df = pd.read_csv('FF_SR_ data.csv')

    #newdf = ffsrdata[(ffsrdata['SR Num_Data_pts'] > 0 ) & (['FF Data_pts'] > 0)]
    newdf = df[(df['SR Num_Data_pts'] > 0) & (df['FF data_points' > 0])]
    return newdf