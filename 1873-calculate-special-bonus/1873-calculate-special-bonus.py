import pandas as pd
import numpy as np
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    is_odd_id = employees['employee_id'] % 2 != 0
    not_start_with_m = ~employees['name'].str.startswith('M')
    
    # 2. Use np.where to assign full salary if both match, else 0
    employees['bonus'] = np.where(is_odd_id & not_start_with_m, employees['salary'], 0)
    
    # 3. Sort by employee_id and select only the requested output columns
    result = employees.sort_values(by='employee_id')[['employee_id', 'bonus']]
    return result