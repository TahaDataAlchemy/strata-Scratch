# Find the number of apartments per nationality that are owned by people under 30 years old.


# Output the nationality along with the number of apartments.


# Sort records by the apartments count in descending order.


import pandas as pd
import numpy as np

merged = pd.merge(airbnb_units, airbnb_hosts, on='host_id')
merged = merged[(merged['age'] < 30) &(merged['unit_type']=='Apartment')]
result = merged.groupby(['nationality'])['unit_id'].nunique().to_frame(
'apartment_count').reset_index().sort_values('apartment_count')
