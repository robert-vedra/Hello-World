import pandas as pd
import plotly.express as px
from datacleaning import clean_dataframe 

df = pd.read_csv('FF_SR_ data.csv')
df = clean_dataframe(df)
SRmean = df['SR Mean per 100g'].astype(float)
FFmean = df['FF Mean per 100g'].astype(float)

vc = df['rank'].value_counts().reset_index()
df['difference'] = (SRmean-FFmean)

#for i in range(len(df)):


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

