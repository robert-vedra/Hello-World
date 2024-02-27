import pandas as pd

df = pd.read_csv('FF_SR_ data.csv')

df['booleancol'] = (df['FF Mean per 100g'] > df['SR Min']) & (df['FF Mean per 100g'] < df['SR Max'])

print(df[df['booleancol'] == True])