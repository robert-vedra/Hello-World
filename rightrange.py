import pandas as pd
import plotly.express as px
from datacleaning import clean_dataframe
from rank_percentdifference import *
from valuecounts import *

df = pd.read_csv('FF_SR_ data.csv')
df = df[df['rank'] != 'sm']
df = clean_dataframe(df)

df['Rank'] = df['rank'].astype(float)

df['booleancol'] = (df['FF Mean per 100g'] > df['SR Min']) & (df['FF Mean per 100g'] < df['SR Max'])

#meanSR v minFF/maxFF -> (abs(meanSR-(nearest boundary)))/(maxFF-minFF)

#if meanSR is less than minFF
toolow = df[df['SR Mean per 100g'] < df['FF Min']]
toolow['Score'] = (toolow['FF Min'] - toolow['SR Mean per 100g'])/(toolow['FF Max']-toolow['FF Min'])
toolow = toolow.sort_values('Rank')

#if meanSR is bigger than maxFF
toohigh = df[df['SR Mean per 100g'] > df['FF Max']]
toohigh['Score'] = ((toohigh['SR Mean per 100g'] - toohigh['FF Max'])/(toohigh['FF Max']-toohigh['FF Min']))
toohigh = toohigh.sort_values('Rank')

fighigh = px.scatter(toohigh, x='Score',y='Rank',title = 'SR Components Above FF Range', hover_name='food_category_id', hover_data='FF_Component')

# fighigh.show()

figlow = px.scatter(toolow, x='Score',y='Rank',title = 'SR Components Below FF Range', hover_name='food_category_id', hover_data='FF_Component')

count = toolow.value_counts('food_category_id')
total = len(toolow)
count = (count/total) * 100
print(count.head)

count2=toohigh.value_counts('food_category_id')
count2 = (count2/len(toohigh)) * 100
print(count2.head())

figlow.show()
fighigh.show()