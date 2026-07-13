import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_data = employee.merge(
    department,
    left_on="departmentId",
    right_on="id")

    max_salary = merged_data.groupby(
        "name_y"
    )["salary"].transform("max")

    result = merged_data[
        merged_data["salary"] == max_salary
    ]

    result = result[
        ["name_y", "name_x", "salary"]
    ]

    result.columns = [
        "Department",
        "Employee",
        "Salary"
    ]

    return result