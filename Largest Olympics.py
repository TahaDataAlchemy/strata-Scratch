# Import your libraries
import pandas as pd

# Start writing code
olympics_athletesCount = olympics_athletes_events.groupby("games")["name"].nunique().reset_index().sort_values(by = "name",ascending = False)

MaxValue = olympics_athletesCount["name"].max()

olympics_athletesCount[olympics_athletesCount["name"] == MaxValue]
