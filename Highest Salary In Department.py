# Import your libraries
import pandas as pd

# Start writing code
departmentSal = employee.groupby(["department"])["salary"].max().reset_index()

employeeSal = employee.groupby(["department","first_name"])["salary"].sum().reset_index()

pd.merge(departmentSal,employeeSal,on = ["department","salary"],how = "inner")
