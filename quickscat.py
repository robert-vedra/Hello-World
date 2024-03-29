import pandas as pd
import plotly.express as px

#get data
df = pd.read_csv('datasets/FF_SR_ data.csv')

SRmean = df['SR Mean per 100g']
FFmean = df['FF Mean per 100g']

vc = df['rank'].value_counts().reset_index()
df['difference'] = (SRmean-FFmean)


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

fig = px.scatter(df, x=df['food_category_id'],y=df['rank'])
fig.show()
