import pandas as pd
import plotly.express as px
from datacleaning import clean_dataframe 

df = pd.read_csv('FF_SR_ data.csv')
df = clean_dataframe(df)

SRmean = df['SR Mean per 100g']
FFmean = df['FF Mean per 100g']

vc = df['rank'].value_counts().reset_index()
df['difference'] = (SRmean-FFmean)

#for i in range(len(df)):


<<<<<<< HEAD:pandasforcsv.py
std = df['difference'].std()
#outliers = df[(df['difference'] > (3*std)) | (df['difference'] < -(3*std))]
sorted = df.sort_values(['rank', 'difference'], ascending = [True, False])
df2 = sorted[['rank','difference',]]
rank = df2.groupby('rank').sum().reset_index()
df3 = rank.merge(vc,on='rank').fillna(0)
df3['mean'] = df3['difference']/df3['count']
outliers = df3[(df3['mean'] > std) | (df3['mean'] < -std)]


#print(first)
#cols = first['FF Food description'],first['difference']
##print(cols)
# fig = px.histogram(df, x=df['FF Food description'],y=df['difference'])
# fig.show()
fig = px.scatter(df3, x=df3['mean'],y=df3['rank'],orientation = 'h')
fig.show()
=======
    vc = df['rank'].value_counts().reset_index()
    df['difference'] = (SRmean-FFmean)
    sorted = df.sort_values(['rank', 'difference'], ascending = [True, False])
    df2 = sorted[['rank','Nutrient_id','difference','FF Mean per 100g']]
    rank = df2.groupby('rank').sum().reset_index()
    df3 = rank.merge(vc,on='rank').fillna(0)

    try:
        df3['rank'] = df3['rank'].astype(int)
    except ValueError:
        pass
    
    df3['percent difference'] = abs(df3['difference']/df3['FF Mean per 100g'])*100
    std = df3['percent difference'].std()

    outliers = df3[(df3['percent difference'] > std) | (df3['percent difference'] < -std)]
    realdata = df3[(df3['percent difference'] < std)]
    realstd = realdata['percent difference'].std()
    outliers = df3[(df3['percent difference'] > realstd)]
    return df3

def find_outliers(df):
    std = df['percent difference'].std()
    outliers = df[(df['percent difference'] > std) | (df['percent difference'] < -std)]
    realdata = df[(df['percent difference'] < std)]
    realstd = realdata['percent difference'].std()
    outliers = df[(df['percent difference'] > realstd)]
    return outliers

def graphdata(df3):
    fig = px.scatter(df3, x=df3['percent difference'],y=df3['rank'],orientation = 'h')
    fig.show()

if __name__ == '__main__':
    df = percent_difference_by_rank()
    outliers = find_outliers(df)
    graphdata(df)

>>>>>>> 7350c5bd7b777ac7c82c615c57f084d99190f3bc:rank_percentdifference.py
