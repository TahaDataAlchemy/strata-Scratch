# You're tasked with analyzing a Spotify-like dataset that captures user listening habits.
# For each user, calculate the total listening time and the count of unique songs they've listened to. In the database duration values are displayed in seconds. Round the total listening duration to the nearest whole minute.


# The output should contain three columns: 'user_id', 'total_listen_duration', and 'unique_song_count'.


# Import your libraries
import pandas as pd

# Start writing code
result = listening_habits.groupby("user_id").agg({
    "song_id": "nunique",
    "listen_duration": "sum"
}).reset_index()

result["listen_duration"] = round(result["listen_duration"]/60,2)

result
