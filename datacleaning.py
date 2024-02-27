import pandas as pd

def clean_dataframe(df):
    df = pd.read_csv('FF_SR_ data.csv')
    newdf = df[(df['SR Num_Data_pts'] > 0) & (df['FF data_points' > 0])]
    return newdf

if __name__ == '__main__':
    df = pd.read_csv('FF_SR_ data.csv')
    ndf = clean_dataframe(df)
    print(ndf)
