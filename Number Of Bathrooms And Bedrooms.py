# Find the average number of bathrooms and bedrooms for each city’s property types. Output the result along with the city name and the property type.

# Import your libraries
import pandas as pd

# Start writing code
Bathroom = airbnb_search_details.groupby(["property_type","city"])["bathrooms"].mean().reset_index()
Bedroom = airbnb_search_details.groupby(["property_type","city"])["bedrooms"].mean().reset_index()

pd.merge(Bathroom,Bedroom,on = ["property_type","city"],how = "inner")
