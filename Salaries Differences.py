# Import your libraries
import pandas as pd

# Assuming db_employee and db_dept are already defined DataFrames

# Merging the employee and department DataFrames
df = pd.merge(db_employee, db_dept, left_on="department_id", right_on="id", how="inner")

# Finding the maximum salary in each department
sal = df.groupby("department")["salary"].max().reset_index()

# Extracting the maximum salary for marketing and engineering departments
Mar_Sal = sal[sal["department"] == "marketing"]["salary"].values[0]
Eng_Sal = sal[sal["department"] == "engineering"]["salary"].values[0]

# Calculating the difference
salary_difference = Mar_Sal - Eng_Sal

salary_difference
