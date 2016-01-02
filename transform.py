import json
from pandas import DataFrame

users = []
nodeIds = []
edgeIds = []

sentiment = DataFrame.from_csv("data/sentiment.csv")

allProfile = DataFrame.from_csv('data/allProfile.csv')
i = 0
for row in allProfile.iterrows():
	if i >= 300:
		break
	thisSent = list(sentiment["label2"])[list(sentiment["id"]).index(row[1]["id"])]
	users.append({"id": row[1]["id"], "followers": row[1]["followers_count"], "friends": row[1]["friends_count"], "sentiment": thisSent})
	nodeIds.append(row[1]["id"])
	i += 1

edges = DataFrame.from_csv('data/edge.csv', index_col=False)

edge = []
for row in edges.iterrows():
	if row[1]["source"] in nodeIds and row[1]["target"] in nodeIds:
		edge.append({"source": row[1]["source"], "target": row[1]["target"]})
		if row[1]["source"] not in edgeIds:
			edgeIds.append(row[1]["source"])
		if row[1]["target"] not in edgeIds:
			edgeIds.append(row[1]["target"])

for i in nodeIds:
	if i not in edgeIds:
		nodeIds.remove(i)

users = [user for user in users if user["id"] in nodeIds]

with open('visualization/sigma.js-1.0.3/examples/nodes.json', 'w') as fp1:
    json.dump(users, fp1)

with open('visualization/sigma.js-1.0.3/examples/edges.json', 'w') as fp2:
    json.dump(edge, fp2)