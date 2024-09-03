# Import your libraries
import pandas as pd

# Start writing code
spotify_worldwide_daily_song_ranking = spotify_worldwide_daily_song_ranking[spotify_worldwide_daily_song_ranking["position"] == 1]

spotify_worldwide_daily_song_ranking.groupby("trackname")["position"].count().reset_index().sort_values(by = "position",ascending = False)
