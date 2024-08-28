# Import your libraries
import pandas as pd

df = pd.merge(facebook_employees,facebook_hack_survey, left_on = "id",right_on = "employee_id",how = "inner")

df.groupby("location")["popularity"].mean().reset_index()
