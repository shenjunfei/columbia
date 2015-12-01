import os
from datetime import datetime
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
#import csv

frequency = {}
info = {"id": [], "total": [], "earliest": [], "latest": []}

for fileName in os.listdir("data/postings"):
	if ".csv" not in fileName:
		continue

	thisId = fileName.replace(".csv", "")
	
	'''
	with open("data/postings/" + fileName, "rb") as f:
		csvreader = csv.reader(f, delimiter=',', quotechar='|')
		for line in csvreader:
			print line
	'''

	try:
		thisFile = DataFrame.from_csv("data/postings/" + fileName)
		thisFile = thisFile[np.isfinite(thisFile["id_str"])]
		num = thisFile.shape[0]

		earliest = datetime.strptime(thisFile["created_at"][num-1], "%a %b %d %H:%M:%S +0000 %Y")
		latest = datetime.strptime(thisFile["created_at"][0], "%a %b %d %H:%M:%S +0000 %Y")

		info["id"].append(thisId)
		info["total"].append(num)
		info["earliest"].append(earliest)
		info["latest"].append(latest)

		for date in thisFile["created_at"]:
			frequency[datetime.strptime(date, "%a %b %d %H:%M:%S +0000 %Y").date()] = frequency.get(datetime.strptime(date, "%a %b %d %H:%M:%S +0000 %Y").date(), 0) + 1
	except:
		continue

DataFrame(info, columns=["id", "total", "earliest", "latest"]).to_csv("info.csv")

date = []
count = []
for key, value in frequency.iteritems():
	date.append(key)
	count.append(value)

plt.plot(date, count, 'ro')
plt.xlabel("date")
plt.ylabel("frequency")
plt.show()

def plot(from_date):
	date = []
	count = []
	for key, value in frequency.iteritems():
		if key >= datetime.strptime(from_date, "%Y-%m-%d").date():
			date.append(key)
			count.append(value)

	plt.plot(date, count, 'ro')
	plt.xlabel("date")
	plt.ylabel("frequency")
	plt.show()

'''
import plotly.plotly as py
import plotly.graph_objs as go
trace = go.Scatter(x = date, y = count)
data = [trace]
py.iplot(data, filename='basic-line')
# alternatively: plot_url = py.plot(data, filename='basic-line')
'''
