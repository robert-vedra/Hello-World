import pandas as pd
from rank_percentdifference import *
#return list of foods that are bad

#get data
df = percent_difference_by_rank()
outliers = find_outliers(df)
print(outliers)

#get list of nutrient ids