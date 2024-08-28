# Import your libraries
import pandas as pd

# Start writing code
Manger13 = salesforce_employees[salesforce_employees["manager_id"] == 13]

Manger13_Sal = Manger13.groupby("first_name")["target"].sum().reset_index().sort_values(by = "target",ascending = False )

Max_Target = Manger13_Sal["target"].max()

Manger13_Sal[Manger13_Sal["target"] == Max_Target]
