import os
import random

net = {}

for user in os.listdir("data/friendships"):
	if user != "empty.txt":
		with open("data/friendships/" + user) as f:
			followers = f.readlines()
			followers = [int(follower.strip()) for follower in followers]
			userId = str(user.replace(".txt", ""))
			net[userId] = followers

print "%d 2nd degree followers." %sum([len(i) for i in net.values()])

total = []
for followers in net.values():
	total += followers

sampled2 = random.sample(total, 30000)

with open("data/sample2.txt" ,'w') as file:
	for item in sampled2:
		print>>file, item

import pandas as pd

df = pd.DataFrame()
get_user_profile(twitter_api, user_ids=sampled2)
df.drop_duplicates(inplace=True)
active = df[df.statuses_count >  5]
english = active[active.lang.isin(en)]
del english["description"]
del english["location"]
del english["name"]
english.to_csv("data/profile2.csv")