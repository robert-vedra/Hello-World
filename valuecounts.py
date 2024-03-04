import pandas as pd

def get_foodcatcounts(catid):
    df = pd.read_csv('FF_SR_ data.csv')
    df = df['food_category_id']
    count = df.value_counts('food_category_id')
    print(count)
get_foodcatcounts('1')

