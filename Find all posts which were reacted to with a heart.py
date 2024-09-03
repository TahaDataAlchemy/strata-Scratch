# Import your libraries
import pandas as pd


df = pd.merge(facebook_reactions,facebook_posts,on = "post_id", how = "inner" )

df = df[df["reaction"] == "heart"]

df[["post_id","poster_y","post_text","post_keywords","post_date"]].drop_duplicates()
