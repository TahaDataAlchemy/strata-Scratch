# Import your libraries
import pandas as pd

# Start writing code
orders["Month"] = orders["order_date"].dt.strftime("%B")

orders = orders[orders["Month"] == "March"]

orders.groupby("cust_id")["total_order_cost"].sum().reset_index()
