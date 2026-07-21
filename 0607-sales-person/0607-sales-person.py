import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merge_orders = pd.merge(orders,company,on="com_id")
    red_saleId = merge_orders[merge_orders["name"]=="RED"]["sales_id"]
    result = sales_person[~sales_person["sales_id"].isin(red_saleId)]
    return result[["name"]]