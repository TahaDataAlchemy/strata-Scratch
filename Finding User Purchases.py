import pandas as pd

amazon_transactions = amazon_transactions.sort_values(by=['user_id', 'created_at'])
amazon_transactions["PreviousDate"] = amazon_transactions.groupby("user_id")["created_at"].shift(1)
amazon_transactions["time_df"] = (amazon_transactions["created_at"] - amazon_transactions["PreviousDate"]).dt.days
df = amazon_transactions[(amazon_transactions["time_df"]<=7)]
df["user_id"].unique()
