# Import your libraries
import pandas as pd

# Start writing code
df = yelp_reviews.groupby(["business_name","review_text"])["cool"].sum().reset_index().sort_values(by = "cool",ascending = False)

df = df[df["cool"] == df["cool"].max()]

df = df[["business_name","review_text"]]
