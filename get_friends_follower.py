from functools import partial
from sys import maxint

def get_friends_followers_ids(twitter_api, screen_name=None, user_id=None, friends_limit=maxint, followers_limit=maxint):
	assert (screen_name != None) != (user_id != None), \
	"Must have screen_name or user_id, but not both"

	get_friends_ids = partial(make_twitter_request, twitter_api.friends.ids, count=5000)
	get_followers_ids = partial(make_twitter_request, twitter_api.followers.ids, count=5000)

	friends_ids, followers_ids = [], []

	for twitter_api_func, limit, ids, label in [
	    [get_friends_ids, friends_limit, friends_ids, "friends"],
	    [get_followers_ids, followers_limit, followers_ids, "followers"]
	]:
		if limit == 0:
			continue

		cursor = -1
		while cursor != 0:
			
			if screen_name:
				response = twitter_api_func(screen_name=screen_name, cursor=cursor)
			else:
				response = twitter_api_func(user_id=user_id, cursor=cursor)

			if response is not None:
				ids += response['ids']
				cursor = response['next_cursor']

			print >> sys.stderr, 'Fetched {0} total {1} ids for {2}'.format(len(ids), label, (user_id or screen_name))

			if len(ids) >= limit or response is None:
				break
	return friends_ids[:friends_limit], followers_ids[:followers_limit]

# Sample usage

twitter_api = oauth_login()

friends_ids, followers_ids = get_friends_followers_ids(twitter_api, screen_name="Columbia", friends_limit=0)

print friends_ids
print followers_ids