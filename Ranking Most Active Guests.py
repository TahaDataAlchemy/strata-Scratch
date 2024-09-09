# Import your libraries
import pandas as pd

# Start writing code
airbnb_contacts_Counts = airbnb_contacts.groupby("id_guest")["n_messages"].sum().reset_index()

# Rank the guests based on the number of messages in descending order
airbnb_contacts_Counts["Rank"] = airbnb_contacts_Counts['n_messages'].rank(ascending=False,method = 'dense').astype(int)

# Sort by 'n_messages' in descending order
sorted_rankings = round(airbnb_contacts_Counts.sort_values(by="n_messages", ascending=False))

# Display the sorted result
