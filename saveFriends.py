from pandas import DataFrame

empty = []

allProfile = DataFrame.from_csv("data/allProfile.csv")
allID = allProfile["id"]

for thisID in list(allID)[2213:]:
    friends_ids, followers_ids = get_friends_followers_ids(twitter_api, user_id=int(thisID), followers_limit=0)
    if len(friends_ids) > 0:
        with open("data/friends/" + str(thisID) + ".txt" ,'w') as file:
            for item in friends_ids:
                print>>file, item
    else:
        empty.append(thisID)

with open("data/friends/empty.txt" ,'w') as file:
    for item in empty:
        print>>file, item
