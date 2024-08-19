
Compare each employee's salary with the average salary of the corresponding department.
Output the department, first name, and salary of employees along with the average salary of that department.



# Import your libraries
import pandas as pd

# Start writing code
employee.head()

dep_Avg = employee.groupby("department")["salary"].mean().reset_index()
Avg_Salary = pd.merge(employee,dep_Avg,on ="department", how = "inner" )

Avg_Salary = Avg_Salary[["department","first_name","salary_x","salary_y"]]

Avg_Salary.columns = ["department","first_name","salary","Avg_Salary"]

Avg_Salary
