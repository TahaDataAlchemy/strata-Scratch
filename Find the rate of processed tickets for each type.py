# Find the rate of processed tickets for each type.

import pandas as pd
import numpy as np

facebook_complaints['processed'] = facebook_complaints['processed'].astype(int)
grouped = facebook_complaints.groupby(['type']).agg({'processed':'sum','complaint_id':'size'}).reset_index()
grouped['processed_rate'] =grouped['processed']/grouped['complaint_id']
result = grouped[['type','processed_rate']]
