from pandas import DataFrame
from datetime import datetime
import numpy as np

allProfile = DataFrame.from_csv("data/allProfile.csv")
allID = allProfile["id"]

day1 = datetime.strptime("2015-11-18", "%Y-%m-%d").date()
day2 = datetime.strptime("2015-11-19", "%Y-%m-%d").date()
day3 = datetime.strptime("2015-11-20", "%Y-%m-%d").date()

allPosts = {"id": allID, "day1": [], "day2": [], "day3": [], "# day1": [], "# day2": [], "# day3": []}

for thisId in allID:
	thisFile = DataFrame.from_csv("data/postings/" + str(thisId) + ".csv")
	thisFile = thisFile[np.isfinite(thisFile["id_str"])]

	i = 0
	posting1 = ""
	numPost1 = 0
	posting2 = ""
	numPost2 = 0
	posting3 = ""
	numPost3 = 0

	for thisDay in thisFile["created_at"]:
		date = datetime.strptime(thisDay, "%a %b %d %H:%M:%S +0000 %Y").date()
		if date > day3:
			i += 1
			continue
		elif date < day1:
			break
		else:
			if date == day1:
				posting1 += thisFile["text"][i]
				posting1 += "\n"
				numPost1 += 1
			elif date == day2:
				posting2 += thisFile["text"][i]
				posting2 += "\n"
				numPost2 += 1
			elif date == day3:
				posting3 += thisFile["text"][i]
				posting3 += "\n"
				numPost3 += 1
			i += 1

	allPosts["day1"].append(posting1)
	allPosts["day2"].append(posting2)
	allPosts["day3"].append(posting3)
	allPosts["# day1"].append(numPost1)
	allPosts["# day2"].append(numPost2)
	allPosts["# day3"].append(numPost3)

DataFrame(allPosts, columns=["id", "# day1", "day1", "# day2", "day2", "# day3", "day3"]).to_csv("data/posts.csv", index=False)