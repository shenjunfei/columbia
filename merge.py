from pandas import DataFrame

profile = DataFrame.from_csv("data/allProfile.csv")
sentiment = DataFrame.from_csv("data/sentiment.csv")
edge = DataFrame.from_csv("data/edge.csv", index_col=False)

ID = list(profile["id"]) # profile and sentiment have same ids in same order

followers = list(profile["followers_count"])
friends = list(profile["friends_count"])
statuses = list(profile["statuses_count"])

label1 = list(sentiment["label1"])
label2 = list(sentiment["label2"])
label3 = list(sentiment["label3"])

neutral1 = list(sentiment["neutral1"])
neutral2 = list(sentiment["neutral2"])
neutral3 = list(sentiment["neutral3"])

pos1 = list(sentiment["pos1"])
pos2 = list(sentiment["pos2"])
pos3 = list(sentiment["pos3"])

sourceFollowers = []
sourceFriends = []
sourceStatuses = []
sourceLab1 = []
sourceLab2 = []
sourceLab3 = []
sourceNeut1 = []
sourceNeut2 = []
sourceNeut3 = []
sourcePos1 = []
sourcePos2 = []
sourcePos3 = []

targetFollwers = []
targetFriends = []
targetStatuses = []
targetLab1 = []
targetLab2 = []
targetLab3 = []
targetNeut1 = []
targetNeut2 = []
targetNeut3 = []
targetPos1 = []
targetPos2 = []
targetPos3 = []

for index, row in edge.iterrows():
	thisSource = row["source"]
	thisTarget = row["target"]

	sourceIndex = ID.index(thisSource)
	targetIndex = ID.index(thisSource)

	sourceFollowers.append(followers[sourceIndex])
	sourceFriends.append(friends[sourceIndex])
	sourceStatuses.append(statuses[sourceIndex])
	sourceLab1.append(label1[sourceIndex])
	sourceLab2.append(label2[sourceIndex])
	sourceLab3.append(label3[sourceIndex])
	sourceNeut1.append(neutral1[sourceIndex])
	sourceNeut2.append(neutral2[sourceIndex])
	sourceNeut3.append(neutral3[sourceIndex])
	sourcePos1.append(pos1[sourceIndex])
	sourcePos2.append(pos2[sourceIndex])
	sourcePos3.append(pos3[sourceIndex])

	targetFollwers.append(followers[targetIndex])
	targetFriends.append(friends[targetIndex])
	targetStatuses.append(statuses[targetIndex])
	targetLab1.append(label1[targetIndex])
	targetLab2.append(label2[targetIndex])
	targetLab3.append(label3[targetIndex])
	targetNeut1.append(neutral1[targetIndex])
	targetNeut2.append(neutral2[targetIndex])
	targetNeut3.append(neutral3[targetIndex])
	targetPos1.append(pos1[targetIndex])
	targetPos2.append(pos2[targetIndex])
	targetPos3.append(pos3[targetIndex])

final = {"source": edge["source"], "target": edge["target"], "sourceFollowers": sourceFollowers, "sourceFriends": sourceFriends, 
         "sourceStatuses": sourceStatuses, "sourceLab1": sourceLab1, "sourceLab2": sourceLab2, "sourceLab3": sourceLab3,
         "sourceNeut1": sourceNeut1, "sourceNeut2": sourceNeut2, "sourceNeut3": sourceNeut3, "sourcePos1": sourcePos1, 
         "sourcePos2": sourcePos2, "sourcePos3": sourcePos3, "targetFollwers": targetFollwers, "targetFriends": targetFriends,
         "targetStatuses": targetStatuses, "targetLab1": targetLab1, "targetLab2": targetLab2, "targetLab3": targetLab3,
         "targetNeut1": targetNeut1, "targetNeut2": targetNeut2, "targetNeut3": targetNeut3, "targetPos1": targetPos1,
         "targetPos2": targetPos2, "targetPos3":targetPos3}
df = DataFrame(final, columns=["source", "target", "sourceFollowers", "sourceFriends", "sourceStatuses", "sourceLab1", "sourceLab2", "sourceLab3",
	"sourceNeut1", "sourceNeut2", "sourceNeut3", "sourcePos1", "sourcePos2", "sourcePos3", "targetFollwers", "targetFriends", "targetStatuses",
	"targetLab1", "targetLab2", "targetLab3", "targetNeut1", "targetNeut2", "targetNeut3", "targetPos1", "targetPos2", "targetPos3"])

df.to_csv("data/final.csv", index=False)