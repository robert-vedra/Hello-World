import pandas as pd

df = pd.read_csv('datasets/FF_SR_ data.csv')
x = df[df['rank'] == 'sm']

