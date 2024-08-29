import pandas as pd

# Start writing code
macbook_device = playbook_events[playbook_events['device']=='macbook pro']
macbook_device.groupby("event_name")["event_type"].count().reset_index().sort_values(by = "event_type",ascending = False)
