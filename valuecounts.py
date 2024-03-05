import pandas as pd

###DO NOT USED###
def get_foodcatcounts(catid):
    df = pd.read_csv('datasets/FF_SR_ data.csv')
    df = df['food_category_id']
    count = df.value_counts('food_category_id')
    print(count)
get_foodcatcounts('1')

