# Method 2: Use the sentiment analysis API, which charges money after exceeding 45000 calls per month
# For common use, each IP has a rate limit of 1000 requests per day

import requests
import ast
from pandas import DataFrame

# Access API in terminal by typing following command:
# curl -d "text=great" http://text-processing.com/api/sentiment/
# Do the same thing in Python with the following code

'''
payload = "text=great"
url = "http://text-processing.com/api/sentiment/"
r = requests.post(url, data=payload)

print r.text
'''

'''
sample output of r.text:

u'{"probability": 
    {"neg": 0.30135019761690551, 
     "neutral": 0.27119050546800266, 
     "pos": 0.69864980238309449}, 
   "label": "pos"}'

u'{"probability": 
    {"neg": 0.434787967754516,
     "neutral": 0.59508906140405482,
     "pos": 0.565212032245484}, 
   "label": "neutral"}'
'''

posts = DataFrame.from_csv("data/posts.csv", index_col=None)
ID = posts["id"]

sentiment = {"id": ID, "label1": [], "neutral1": [], "pos1": [], "neg1": [],
                       "label2": [], "neutral2": [], "pos2": [], "neg2": [],
                       "label3": [], "neutral3": [], "pos3": [], "neg3": []}

url = "http://text-processing.com/api/sentiment/"

i = 0

for thisID in ID:

	text1 = "text=" + posts["day1"][i]
	analysis1 = requests.post(url, data=text1)
	try:
		parse1 = ast.literal_eval(analysis1.text)
		sentiment["label1"].append(parse1["label"])
		sentiment["neutral1"].append(parse1["probability"]["neutral"])
		sentiment["pos1"].append(parse1["probability"]["pos"])
		sentiment["neg1"].append(parse1["probability"]["neg"])
	except:
		sentiment["label1"].append(analysis1)
		sentiment["neutral1"].append(0)
		sentiment["pos1"].append(0)
		sentiment["neg1"].append(0)

	text2 = "text=" + posts["day2"][i]
	analysis2 = requests.post(url, data=text2)
	try:
		parse2 = ast.literal_eval(analysis2.text)
		sentiment["label2"].append(parse2["label"])
		sentiment["neutral2"].append(parse2["probability"]["neutral"])
		sentiment["pos2"].append(parse2["probability"]["pos"])
		sentiment["neg2"].append(parse2["probability"]["neg"])
	except:
		sentiment["label2"].append(analysis2)
		sentiment["neutral2"].append(0)
		sentiment["pos2"].append(0)
		sentiment["neg2"].append(0)

	text3 = "text=" + posts["day3"][i]
	analysis3 = requests.post(url, data=text3)
	try:
		parse3 = ast.literal_eval(analysis3.text)
		sentiment["label3"].append(parse3["label"])
		sentiment["neutral3"].append(parse3["probability"]["neutral"])
		sentiment["pos3"].append(parse3["probability"]["pos"])
		sentiment["neg3"].append(parse3["probability"]["neg"])
	except:
		sentiment["label3"].append(analysis3.text)
		sentiment["neutral3"].append(0)
		sentiment["pos3"].append(0)
		sentiment["neg3"].append(0)

	i += 1

df = DataFrame(sentiment, columns=["id", "label1", "neutral1", "pos1", "neg1", "label2", "neutral2", "pos2", "neg2", "label3", "neutral3", "pos3", "neg3"])
df.to_csv("data/sentiment.csv")
