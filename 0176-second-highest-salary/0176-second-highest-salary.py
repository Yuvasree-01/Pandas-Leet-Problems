import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salary = employee["salary"].drop_duplicates()
    second_highest_salary = unique_salary.sort_values(ascending=False)
    if len(second_highest_salary)<2:
        return pd.DataFrame({"SecondHighestSalary":[None]})


    result=second_highest_salary.iloc[1]
    return pd.DataFrame({"SecondHighestSalary":[result]})