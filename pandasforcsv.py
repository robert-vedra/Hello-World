import pandas as pd
import plotly.express as px

df = pd.read_csv('FF_SR_ data.csv')
SRmean = df['SR Mean per 100g']
FFmean = df['FF Mean per 100g']

df['difference'] = SRmean-FFmean
std = df['difference'].std()
outliers = df[(df['difference'] > (3*std)) | (df['difference'] < -(3*std))]
#sorted = outliers.sort_values(['FF Food description', 'difference'], ascending = [True, False])
#first = sorted.groupby('FF Food description').first().reset_index()
#print(first)
#cols = first['FF Food description'],first['difference']
##print(cols)
fig = px.histogram(df, x=df['FF Food description'],y=df['difference'])
fig.show()
fig = px.histogram(df, x=df['Nutrient_id'],y=df['difference'])
fig.show()
