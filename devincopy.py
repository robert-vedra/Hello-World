import pandas as pd
import plotly.express as px

df = pd.read_csv('FF_SR_ data.csv')
SRmean = df['SR Mean per 100g']
FFmean = df['FF Mean per 100g']

vc = df['Nutrient_id'].value_counts().reset_index()
df['difference'] = (SRmean-FFmean)

#for i in range(len(df)):


std = df['difference'].std()
#outliers = df[(df['difference'] > (3*std)) | (df['difference'] < -(3*std))]
df2 = df.sort_values(['Nutrient_id', 'difference'], ascending = [True, False])
# = sorted[['Nutrient_id','difference']]
rank = df2.groupby('Nutrient_id').sum().reset_index()
df3 = rank.merge(vc,on='Nutrient_id').fillna(0)
df3['mean'] = df3['difference']/df3['count']
outliers = df3[(df3['mean'] > std) | (df3['mean'] < -std)]


#print(first)
#cols = first['FF Food description'],first['difference']
##print(cols)
# fig = px.histogram(df, x=df['FF Food description'],y=df['difference'])
# fig.show()
fig = px.scatter(df3, x=df3['mean'],y=df3['Nutrient_id'],orientation = 'h')
fig.show()