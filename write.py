import pickle
import random

with open("data/ID.txt", 'wb') as f:
    pickle.dump(followers_ids, f)

with open("data/ID50000", 'rb') as f:
    followers_ids = pickle.load(f)

sampled_ids = random.sample(followers_ids, 10000)

with open("data/sampled_ids", 'wb') as f:
    pickle.dump(sampled_ids, f)

with open("data/sampled_ids", 'rb') as f:
    my_list = pickle.load(f)


empty = []

for thisID in sampled_id:
	friends_ids, followers_ids = get_friends_followers_ids(twitter_api, user_id=int(thisID), friends_limit=0, followers_limit=10000)
	if len(followers_ids) > 0:
		with open("data/friendships/" + str(thisID) + ".txt" ,'w') as file:
			for item in followers_ids:
				print>>file, item
	else:
		empty.append(thisID)

with open("data/friendships/empty.txt" ,'w') as file:
	for item in empty:
		print>>file, item