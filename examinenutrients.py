import pandas as pd
import plotly.express as px
from datacleaning import clean_dataframe


#import and clean dataframe
df = pd.read_csv('datasets/FF_SR_ data.csv')
df = clean_dataframe(df)

#determine what the SR and FF means are
SRmean = df['SR Mean per 100g']
FFmean = df['FF Mean per 100g']

#print nutrient ids and a value count of each
vc = df['Nutrient_id'].value_counts().reset_index()
df['difference'] = (SRmean-FFmean)

#find standard deviation --> used to find nutrients that are 'abnormal'
std = df['difference'].std()

#create new df, sortednutid, which is df sorted by the nutrient id
sortednutid = df.sort_values(['Nutrient_id', 'difference'], ascending = [True, False])

# 
rank = sortednutid.groupby('Nutrient_id').sum().reset_index()

#create new df, finaldf, that has nutrient_id and difference. Frome here determine outliers
finaldf = rank.merge(vc,on='Nutrient_id').fillna(0)
finaldf['mean'] = finaldf['difference']/finaldf['count']
outliers = finaldf[(finaldf['mean'] > .5*std) | (finaldf['mean'] < .5*-std)]

#show scatterplot
fig = px.scatter(finaldf, x=finaldf['mean'],y=finaldf['Nutrient_id'],orientation = 'h')
fig.show()


