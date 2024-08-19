# Find the details of each customer regardless of whether the customer made an order. Output the customer's first name, last name, and the city along with the order details.
# Sort records based on the customer's first name and the order details in ascending order.


# Import your libraries
import pandas as pd

# Start writing code
merged_df = pd.merge(customers, orders, left_on="id", right_on="cust_id", how="left")

# Sorting by 'first_name' from customers and 'order_details' from orders
sorted_df = merged_df.sort_values(by=["first_name", "order_details"]).reset_index(drop=True)

sorted_df[["first_name","last_name","city","order_details"]]
