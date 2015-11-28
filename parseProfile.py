import json
import numpy as np
import pandas as pd

def profile_df(profiles):
	df = pd.DataFrame(profiles, columns=["id", "screen_name", "name", "lang", "created_at", "location", "time_zone", "description", "followers_count", "friends_count", "statuses_count"])
	return df

df.to_csv("data/profile.csv")

pd.concat([df1, df2, df3])

df = pd.DataFrame()
get_user_profile(twitter_api, user_ids=followers_ids)
df.drop_duplicates(inplace = True)

del df["description"]
del df["location"]
del df["name"]