# What were the top 10 ranked songs in 2010?
# Output the rank, group name, and song name but do not show the same song twice.
# Sort the result based on the year_rank in ascending order.

# # Import your libraries
import pandas as pd

# Start writing code
df = billboard_top_100_year_end[billboard_top_100_year_end["year"] == 2010]

df.drop_duplicates(subset = "song_name",inplace = True)

df.sort_values(by = "year_rank",ascending = True)

df[["year_rank","group_name","song_name"]].head(10)
