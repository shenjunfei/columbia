empty = []

for thisId in id:
	harvest_user_timeline(twitter_api, user_id=thisId, max_results=200)

with open("data/postings/empty.txt" ,'w') as file:
	for item in empty:
		print>>file, item