# Import your libraries
import pandas as pd

# Start writing code
energy_merge = pd.merge(fb_eu_energy,fb_asia_energy,on = "date",how = "outer").fillna(0)

energy_merge.columns = ["date","eu_energy","asia_energy"]

energy_merge = pd.merge(energy_merge,fb_na_energy,on = "date",how = "outer").fillna(0)

energy_merge.columns = ["date","eu_energy","asia_energy","na_energy"]
energy_merge["Consumption"] = energy_merge["eu_energy"] + energy_merge["asia_energy"] + energy_merge["na_energy"]
energy_merge = energy_merge[["date","Consumption"]]

energy_merge.sort_values(by = "Consumption",ascending = False).head(2)
