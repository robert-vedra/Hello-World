import pandas as pd

#input rank and return entry
rank = input('rank:')
df = pd.read_csv('datasets/FF_SR_ data.csv')
entry = df[df['rank'] == rank]

