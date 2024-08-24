import pandas as pd

# Assuming sf_restaurant_health_violations is already loaded as a DataFrame

# Convert all business names to lowercase to ensure consistent matching
sf_restaurant_health_violations["business_name"] = sf_restaurant_health_violations["business_name"].str.lower()

# Classify businesses based on keywords in the business name
def classify(name):
    if "restaurant" in name:
        return "restaurant"
    elif "cafe" in name or "café" in name or "coffee" in name:
        return "cafe"
    elif "school" in name:
        return "school"
    else:
        return "other"
sf_restaurant_health_violations["business_type"] = sf_restaurant_health_violations["business_name"].apply(classify) 

    
# Drop duplicates and display the relevant columns
output = sf_restaurant_health_violations[["business_name", "business_type"]].drop_duplicates()

# Display the output DataFrame
