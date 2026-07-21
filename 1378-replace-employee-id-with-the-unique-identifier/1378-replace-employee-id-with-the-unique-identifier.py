import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merge_data = pd.merge(employees,employee_uni,on="id",how="left")
    return merge_data[["unique_id","name"]]