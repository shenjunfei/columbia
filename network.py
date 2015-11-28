from pandas import DataFrame

source = []
target = []

ColumbiaId = 248795646

for id in userId:
	source.append(id)
	target.append(ColumbiaId)

for id in sampled:
	for thisUser, thisFollower in net.iteritems():
		if id in thisFollower:
			source.append(id)
			target.append(thisUser)

net = {"source": source, "target": target}
df = DataFrame(net)
df.to_csv("data/edge.csv")