import pandas as pd
import plotly.express as px
from datacleaning import clean_dataframe

df = pd.read_csv('FF_SR_ data.csv')
df = df[df['rank'] != 'sm']
#df = clean_dataframe(df)

df['rank'] = df['rank'].astype(float)

r = df['rank'].iloc[5]

print(r)

df['booleancol'] = (df['FF Mean per 100g'] > df['SR Min']) & (df['FF Mean per 100g'] < df['SR Max'])

#meanSR v minFF/maxFF -> (abs(meanSR-(nearest boundary)))/(maxFF-minFF)

#if meanSR is less than minFF
toolow = df[df['SR Mean per 100g'] < df['FF Min']]
toolow['score'] = (toolow['FF Min'] - toolow['SR Mean per 100g'])/(toolow['FF Max']-toolow['FF Min'])
toolow = toolow.sort_values('rank')

#if meanSR is bigger than maxFF
toohigh = df[df['SR Mean per 100g'] > df['FF Max']]
toohigh['score'] = ((toohigh['SR Mean per 100g'] - toohigh['FF Max'])/(toohigh['FF Max']-toohigh['FF Min']))
toohigh = toohigh.sort_values('rank')



fighigh = px.scatter(df, x=toohigh['score'],y=toohigh['rank'])

fighigh.show()

figlow = px.scatter(df, x=toolow['score'],y=toolow['rank'])

figlow.show()