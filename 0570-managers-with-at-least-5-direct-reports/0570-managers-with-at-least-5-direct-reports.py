import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    manager_count = employee["managerId"].value_counts()
    high_count = manager_count[manager_count>=5].index
    result = employee[employee['id'].isin(high_count)]

    return result[["name"]]