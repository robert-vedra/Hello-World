import pandas as pd
import plotly.express as px
from datacleaning import clean_dataframe 

df = pd.read_csv('datasets/FF_SR_ data.csv')
df = clean_dataframe(df)

# SRmean = df['SR Mean per 100g']
# FFmean = df['FF Mean per 100g']

# vc = df['rank'].value_counts().reset_index()
# df['difference'] = (SRmean-FFmean)

# #for i in range(len(df)):


# std = df['difference'].std()
# #outliers = df[(df['difference'] > (3*std)) | (df['difference'] < -(3*std))]
# sorted = df.sort_values(['rank', 'difference'], ascending = [True, False])
# df2 = sorted[['rank','difference',]]
# rank = df2.groupby('rank').sum().reset_index()
# df3 = rank.merge(vc,on='rank').fillna(0)
# df3['mean'] = df3['difference']/df3['count']
# outliers = df3[(df3['mean'] > std) | (df3['mean'] < -std)]


#print(first)
#cols = first['FF Food description'],first['difference']
##print(cols)
# fig = px.histogram(df, x=df['FF Food description'],y=df['difference'])
# fig.show()
#fig = px.scatter(df3, x=df3['mean'],y=df3['rank'],orientation = 'h')
#fig.show()

def percent_difference_by_rank():
    df = pd.read_csv('datasets/FF_SR_ data.csv')
    df = clean_dataframe(df)
    SRmean = df['SR Mean per 100g']
    FFmean = df['FF Mean per 100g']

    vc = df['rank'].value_counts().reset_index()
    df['difference'] = (SRmean-FFmean)
    sorted = df.sort_values(['rank', 'difference'], ascending = [True, False])
    df2 = sorted[['rank','FF_Component','difference','FF Mean per 100g']]
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

def find_outliers(df,columname):
    std = df[columname].std()
    outliers = df[(df[columname] > std) | (df[columname] < -std)]
    realdata = df[(df[columname] < std)]
    realstd = realdata[columname].std()
    outliers = df[(df[columname] > realstd)]
    return outliers

def graphdata(df3):
    fig = px.scatter(df3, x=df3['percent difference'],y=df3['rank'], hover_name= df3['FF_Component'], orientation = 'h')
    fig.show()

if __name__ == '__main__':
    df = percent_difference_by_rank()
    outliers = find_outliers(df)
    graphdata(df)
    nutrient1_count = outliers['FF_Component'].value_counts()
    print(nutrient1_count)