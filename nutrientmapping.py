import pandas as pd
from rank_percentdifference import *
#return list of foods that are bad

#get data
df2 = 
df = percent_difference_by_rank()
outliers = find_outliers(df)

#list of outliers:
outlierslist = outliers['FF_Component'].tolist()

for nutrient in outlierslist:
    print(outliers[outliers['FF_Description']==nutrient])
    



#get list of nutrient ids