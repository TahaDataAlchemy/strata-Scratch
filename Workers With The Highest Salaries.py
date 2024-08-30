# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(worker,title,left_on = "worker_id",right_on = "worker_ref_id",how = "inner")
MaxSal = df.groupby("worker_title")["salary"].max().reset_index()

result = pd.merge(df, MaxSal, on=["worker_title", "salary"], how="inner")
MAX = result["salary"].max()

result[result["salary"] == MAX]["worker_title"]
