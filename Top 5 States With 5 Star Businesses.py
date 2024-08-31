import pandas as pd

# Assuming 'yelp_business' is your DataFrame
yelp_5star = yelp_business[yelp_business["stars"] == 5]

# Group by 'state' and count the number of 5-star businesses per state
yelp_5star_count = yelp_5star.groupby("state")["stars"].count().reset_index().sort_values(by =["stars","state"],ascending = [False,True]).rename(columns = {"stars":"CountOf5starRestaurant"})

Max_Count_Till5 = yelp_5star_count["CountOf5starRestaurant"].iloc[4]

yelp_5star_count[yelp_5star_count["CountOf5starRestaurant"]>= Max_Count_Till5]
