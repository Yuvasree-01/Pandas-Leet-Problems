import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salary = employee["salary"].drop_duplicates()
    sorted_salary = unique_salary.sort_values(ascending=False)
    if N>len(sorted_salary) or N<=0:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})
    nth_highest = sorted_salary.iloc[N-1]
    return pd.DataFrame({f'getNthHighestSalary({N})':[nth_highest]})