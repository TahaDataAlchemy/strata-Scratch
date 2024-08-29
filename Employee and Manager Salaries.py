import pandas as pd

# Filter for managers and employees
joined_data = employee.merge(employee, left_on='manager_id', right_on='id', suffixes=('_employee', '_manager'))
joined_data[joined_data["salary_employee"] > joined_data["salary_manager"]][["first_name_employee","salary_employee"]]
