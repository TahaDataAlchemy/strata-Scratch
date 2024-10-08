# We have a table with employees and their salaries, however, some of the records are old and contain outdated salary information. Find the current salary of each employee assuming that salaries increase each year. Output their id, first name, last name, department ID, and current salary. Order your list by employee ID in ascending order.


# Import your libraries
import pandas as pd
# Start writing code
ms_employee_salary["Full_Name"] = ms_employee_salary["first_name"] + "_" + ms_employee_salary["last_name"]

ms_employee = ms_employee_salary.groupby("Full_Name")["salary"].max().reset_index()

filtered_df = pd.merge(ms_employee_salary, ms_employee, on=["Full_Name", "salary"])
filtered_df[["id","first_name","last_name","department_id","salary"]]
