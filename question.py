import pandas as pd

df = pd.read_csv('FF_SR_ data.csv')
x = df[df['rank'] == 7220]
print(x.iloc[1])