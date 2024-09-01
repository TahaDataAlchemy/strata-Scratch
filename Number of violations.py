# Import your libraries
import pandas as pd

# Start writing code'
Roxanne = sf_restaurant_health_violations[sf_restaurant_health_violations["business_name"] == 'Roxanne Cafe']

Roxanne["year"] = Roxanne["inspection_date"].dt.year
Roxanne.groupby("year")["violation_id"].count().reset_index().sort_values(by = "year",ascending = True)
