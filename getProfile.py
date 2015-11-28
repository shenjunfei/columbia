def get_user_profile(twitter_api, screen_names=None, user_ids=None):
	
	assert (screen_names != None) != (user_ids != None), \
	"Must have screen_names or user_ids, but not both"

	items_to_info = []

	items = screen_names or user_ids

	while len(items) > 0:

		items_str = ','.join([str(item) for item in items[:100]])

		items = items[100:]

		if screen_names:
			response = make_twitter_request(twitter_api.users.lookup, screen_name=items_str)

		else:
			response = make_twitter_request(twitter_api.users.lookup, user_id=items_str)

		for user_info in response:
			if screen_names:
				items_to_info.append(user_info)
				#items_to_info[user_info['screen_name']] = user_info
			else:
				items_to_info.append(user_info)
				#items_to_info[user_info['id']] = user_info

		global df
		df = pd.concat([df, pd.DataFrame(items_to_info, columns=["id", "screen_name", "name", "lang", "created_at", "location", "time_zone", "description", "followers_count", "friends_count", "statuses_count"])])

		#return items_to_info

# Sample usage

twitter_api = oauth_login()

print get_user_profile(twitter_api, screen_names=["SocialWebMining", "ptwobrussell"])


'''
{u'ptwobrussell': {u'contributors_enabled': False,
  u'created_at': u'Tue Feb 05 08:16:12 +0000 2008',
  u'default_profile': False,
  u'default_profile_image': False,
  u'description': u'Computer Scientist. Technologist. CrossFitter. Triathlete. Author.',
  u'entities': {u'description': {u'urls': []},
   u'url': {u'urls': [{u'display_url': u'MiningTheSocialWeb.com',
      u'expanded_url': u'http://MiningTheSocialWeb.com',
      u'indices': [0, 22],
      u'url': u'http://t.co/AzFoM9TBPO'}]}},
  u'favourites_count': 906,
  u'follow_request_sent': False,
  u'followers_count': 1941,
  u'following': True,
  u'friends_count': 164,
  u'geo_enabled': False,
  u'has_extended_profile': False,
  u'id': 13085242,
  u'id_str': u'13085242',
  u'is_translation_enabled': False,
  u'is_translator': False,
  u'lang': u'en',
  u'listed_count': 166,
  u'location': u'Franklin, TN',
  u'name': u'Matthew Russell',
  u'notifications': False,
  u'profile_background_color': u'888888',
  u'profile_background_image_url': u'http://pbs.twimg.com/profile_background_images/112353046/twitter-1.4.2.gif',
  u'profile_background_image_url_https': u'https://pbs.twimg.com/profile_background_images/112353046/twitter-1.4.2.gif',
  u'profile_background_tile': False,
  u'profile_image_url': u'http://pbs.twimg.com/profile_images/378800000365424290/cbdedf17eb021ce95ddce059a90c1787_normal.jpeg',
  u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/378800000365424290/cbdedf17eb021ce95ddce059a90c1787_normal.jpeg',
  u'profile_link_color': u'EE8336',
  u'profile_sidebar_border_color': u'888888',
  u'profile_sidebar_fill_color': u'F7F7F7',
  u'profile_text_color': u'333333',
  u'profile_use_background_image': True,
  u'protected': False,
  u'screen_name': u'ptwobrussell',
  u'status': {u'contributors': None,
   u'coordinates': None,
   u'created_at': u'Mon Aug 17 14:42:52 +0000 2015',
   u'entities': {u'hashtags': [],
    u'symbols': [],
    u'urls': [{u'display_url': u'ngdata.com/top-data-scien\u2026',
      u'expanded_url': u'http://www.ngdata.com/top-data-science-resources/',
      u'indices': [117, 139],
      u'url': u'http://t.co/FbBvPJW9tl'}],
    u'user_mentions': [{u'id': 132373965,
      u'id_str': u'132373965',
      u'indices': [3, 19],
      u'name': u'MiningTheSocialWeb',
      u'screen_name': u'SocialWebMining'}]},
   u'favorite_count': 0,
   u'favorited': False,
   u'geo': None,
   u'id': 633287885244887041,
   u'id_str': u'633287885244887041',
   u'in_reply_to_screen_name': None,
   u'in_reply_to_status_id': None,
   u'in_reply_to_status_id_str': None,
   u'in_reply_to_user_id': None,
   u'in_reply_to_user_id_str': None,
   u'lang': u'en',
   u'place': None,
   u'possibly_sensitive': False,
   u'retweet_count': 13,
   u'retweeted': False,
   u'retweeted_status': {u'contributors': None,
    u'coordinates': None,
    u'created_at': u'Thu Mar 05 23:39:56 +0000 2015',
    u'entities': {u'hashtags': [],
     u'symbols': [],
     u'urls': [{u'display_url': u'ngdata.com/top-data-scien\u2026',
       u'expanded_url': u'http://www.ngdata.com/top-data-science-resources/',
       u'indices': [96, 118],
       u'url': u'http://t.co/FbBvPJW9tl'}],
     u'user_mentions': []},
    u'favorite_count': 30,
    u'favorited': False,
    u'geo': None,
    u'id': 573629045113401344,
    u'id_str': u'573629045113401344',
    u'in_reply_to_screen_name': None,
    u'in_reply_to_status_id': None,
    u'in_reply_to_status_id_str': None,
    u'in_reply_to_user_id': None,
    u'in_reply_to_user_id_str': None,
    u'lang': u'en',
    u'place': None,
    u'possibly_sensitive': False,
    u'retweet_count': 13,
    u'retweeted': False,
    u'source': u'<a href="https://about.twitter.com/products/tweetdeck" rel="nofollow">TweetDeck</a>',
    u'text': u'A curation of the "Top 50 Data Science Resources". \n\nMining the Social Web checks in at  #10! \n\nhttp://t.co/FbBvPJW9tl',
    u'truncated': False},
   u'source': u'<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>',
   u'text': u'RT @SocialWebMining: A curation of the "Top 50 Data Science Resources". \n\nMining the Social Web checks in at  #10! \n\nhttp://t.co/FbBvPJW9tl',
   u'truncated': False},
  u'statuses_count': 1508,
  u'time_zone': u'Central Time (US & Canada)',
  u'url': u'http://t.co/AzFoM9TBPO',
  u'utc_offset': -21600,
  u'verified': False}}
'''