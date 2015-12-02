# Method 1: Use the open source package TextBlob

from pandas import DataFrame
from textblob import TextBlob

posts = DataFrame.from_csv("data/posts.csv", index_col=None)
ID = posts["id"]

sentiment = {"id": ID, "polarity1": [], "subjuectivity1": [], "polarity2": [], "subjuectivity2": [], "polarity3": [], "subjuectivity3": []}

i = 0
for thisID in ID:
	analysis1 = TextBlob(posts["day1"][i]).sentiment
	sentiment["polarity1"].append(analysis1.polarity)
	sentiment["subjuectivity1"].append(analysis1.subjuectivity)

	analysis2 = TextBlob(posts["day2"][i]).sentiment
	sentiment["polarity2"].append(analysis2.polarity)
	sentiment["subjuectivity2"].append(analysis2.subjuectivity)

	analysis3 = TextBlob(posts["day3"][i]).sentiment
	sentiment["polarity3"].append(analysis3.polarity)
	sentiment["subjuectivity3"].append(analysis3.subjuectivity)

	i += 1

# This does not support unicode encoding?

DataFrame(sentiment, columns=["id", "polarity1", "subjuectivity1", "polarity2", "subjuectivity2", "polarity3", "subjuectivity3"]).to_csv("data/sentiment.csv")