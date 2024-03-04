import pandas as pd
from rank_percentdifference import *

###NOT IN USE####



#get data
df = percent_difference_by_rank()
outliers = find_outliers(df)

#list of outliers:
outlierslist = outliers['FF_Component'].tolist()

for nutrient in outlierslist:
    print(outliers[outliers['FF_Description']==nutrient])
