import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    cus_counts = orders.groupby('customer_number').size()
    top_cus = cus_counts.idxmax()
    return pd.DataFrame({'customer_number': [top_cus]})