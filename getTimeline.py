from pandas import DataFrame

def harvest_user_timeline(twitter_api, screen_name=None, user_id=None, max_results=1000):

	assert (screen_name != None) != (user_id != None), \
	"Must have screen_name or user_id, but not both"

	kw = {'count': 200,
	      'trim_user': 'true',
	      'include_rts' : 'true',
	      'since_id' : 1
	      }

	if screen_name:
		kw['screen_name'] = screen_name
	else:
		kw['user_id'] = user_id

	max_pages = 16
	results = []

	tweets = make_twitter_request(twitter_api.statuses.user_timeline, **kw)

	if tweets is None:
		tweets = []

	results += tweets

	print >> sys.stderr, 'Fetched %i tweets for %d' % (len(tweets), user_id)

	page_num = 1

	if max_results == kw['count']:
		page_num = max_pages

	while page_num < max_pages and len(tweets) > 0 and len(results) < max_results:

		kw['max_id'] = min([ tweet['id'] for tweet in tweets]) - 1

		tweets = make_twitter_request(twitter_api.statuses.user_timeline, **kw)
		results += tweets

		print >> sys.stderr, 'Fetched %i tweets for %d' % (len(tweets), user_id)

		page_num += 1

	print >> sys.stderr, 'Done fetching tweets'

	if len(tweets) == 0:
		global empty
		empty.append(user_id)
	else:
		df = DataFrame(results[:max_results], columns=["id_str", "created_at", "retweet_count", "favorite_count", "text"])
		df.to_csv("data/postings/" + str(user_id) + ".csv", encoding='utf-8')
	

# Sample usage

twitter_api = oauth_login()
tweets = harvest_user_timeline(twitter_api, screen_name="SocialWebMining", max_results=200)
# Save to MongoDB with save_to_mongo or a local file with save_json...