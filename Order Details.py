# Import your libraries
import pandas as pd

# Start writing code
dataset = pd.merge(customers,orders, left_on = "id",right_on = "cust_id",how = "inner").reset_index()

dataset = dataset[(dataset["first_name"] == "Jill") | (dataset["first_name"] == "Eva")]

dataset.groupby(["order_date","order_details","first_name"])["total_order_cost"].sum().reset_index()
