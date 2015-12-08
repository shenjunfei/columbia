from pandas import DataFrame
import os

source = []
target = []

# "source" is the user who follows others, while "target" is the user who is being followed

allProfile = DataFrame.from_csv("data/allProfile.csv")
ID = list(allProfile["id"])

edges = DataFrame.from_csv("data/edge1.csv")

for index, row in edges.iterrows():
	if row["source"] in ID and row["target"] in ID:
		source.append(row["source"])
		target.append(row["target"])

print "%d connections obtained from previous record." %len(source)

files = []

for file in os.listdir("data/friends"):
    if file.endswith(".txt"):
        files.append(file)

i = 0

for thisFile in files:
	thisId = int(thisFile.replace(".txt", ""))
	d = DataFrame.from_csv("data/friends/" + thisFile)
	ids = list(d.index)
	for thisFriend in ids:
		if thisFriend in ID:
			i += 1
			source.append(thisId)
			target.append(thisFriend)

print "%d connections obtained from new friends list." %i

net = {"source": source, "target": target}
df = DataFrame(net, columns=["source", "target"])
df.drop_duplicates(inplace=True)
df.to_csv("data/edge.csv", index=False)