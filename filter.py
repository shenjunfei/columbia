import os
from datetime import datetime
from pandas import DataFrame
import pandas as pd
import numpy as np

day1 = datetime.strptime("2015-11-18", "%Y-%m-%d").date()
day2 = datetime.strptime("2015-11-19", "%Y-%m-%d").date()
day3 = datetime.strptime("2015-11-20", "%Y-%m-%d").date()
day4 = datetime.strptime("2015-11-21", "%Y-%m-%d").date()
day5 = datetime.strptime("2015-11-22", "%Y-%m-%d").date()
day6 = datetime.strptime("2015-11-23", "%Y-%m-%d").date()
day7 = datetime.strptime("2015-11-24", "%Y-%m-%d").date()

post = {day1: [], day2: [], day3: [], day4: [], day5: [], day6: [], day7: []}

for fileName in os.listdir("data/postings"):
	if ".csv" not in fileName:
		continue

	thisId = int(fileName.replace(".csv", ""))

	try:
		thisFile = DataFrame.from_csv("data/postings/" + fileName)
		thisFile = thisFile[np.isfinite(thisFile["id_str"])]
		
		for date in thisFile["created_at"]:
			thisDay = datetime.strptime(date, "%a %b %d %H:%M:%S +0000 %Y").date()
			if thisDay > day7:
				continue
			elif thisDay < day1:
				break
			else:
				if len(post[thisDay]) > 0:
					if post[thisDay][-1] != thisId:
						post[thisDay].append(thisId)
				else:
					post[thisDay].append(thisId)
	except:
		continue

for key, value in post.iteritems():
	DataFrame(value).to_csv("data/" + key.strftime('%m-%d-%Y') + '.csv', index=False)

len(list(set(post[day1]) & set(post[day2]) & set(post[day3]) & set(post[day4]) & set(post[day5]) & set(post[day6]) & set(post[day7]))) # 2084

len(list(set(post[day1]) & set(post[day2]) & set(post[day3]) & set(post[day4]) & set(post[day5]) & set(post[day6]))) # 2551

len(list(set(post[day2]) & set(post[day3]) & set(post[day4]) & set(post[day5]) & set(post[day6]) & set(post[day7]))) # 2284

len(list(set(post[day1]) & set(post[day2]) & set(post[day3]) & set(post[day4]) & set(post[day5]))) # 2722

len(list(set(post[day2]) & set(post[day3]) & set(post[day4]) & set(post[day5]) & set(post[day6]))) # 2835

len(list(set(post[day3]) & set(post[day4]) & set(post[day5]) & set(post[day6]) & set(post[day7]))) # 2523

len(list(set(post[day1]) & set(post[day2]) & set(post[day3]) & set(post[day4]))) # 3178

len(list(set(post[day2]) & set(post[day3]) & set(post[day4]) & set(post[day5]))) # 3053

len(list(set(post[day3]) & set(post[day4]) & set(post[day5]) & set(post[day6]))) # 3136

len(list(set(post[day4]) & set(post[day5]) & set(post[day6]) & set(post[day7]))) # 2789

len(list(set(post[day1]) & set(post[day2]) & set(post[day3]))) # 4055 choose this

len(list(set(post[day2]) & set(post[day3]) & set(post[day4]))) # 3632

len(list(set(post[day3]) & set(post[day4]) & set(post[day5]))) # 3437

len(list(set(post[day4]) & set(post[day5]) & set(post[day6]))) # 3534

len(list(set(post[day5]) & set(post[day6]) & set(post[day7]))) # 3238


selectedID = list(set(post[day1]) & set(post[day2]) & set(post[day3]))

sample1000 = DataFrame.from_csv("data/sample1000.csv")

selected1000 = sample1000[sample1000.id.isin(selectedID)] # 125 obs. Inspiring!

sample2 = DataFrame.from_csv("data/profile2.csv")

selected2 = sample2[sample2.id.isin(selectedID)] # 3977 obs

allObjects = pd.concat([selected1000, selected2])

allObjects.to_csv("data/allProfile.csv")
