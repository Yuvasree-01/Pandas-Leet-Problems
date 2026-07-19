import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = activities.drop_duplicates(subset=['sell_date', 'product']).sort_values(by='product')
    result=df.groupby(['sell_date'],as_index=False).agg(num_sold=('product','nunique'),products=('product',lambda x: ','.join(x)))
    return result