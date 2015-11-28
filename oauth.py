import twitter

def oauth_login():
	CONSUMER_KEY = 'bVlW676e7Zrscdv6nmHDKxnNJ'
	CONSUMER_SECRET = 'Nkz6BiQiZ2Dxwc1X2TuLMzxpcI9rmPd6cqeDvRQ6tQJv55gJ03'
	OAUTH_TOKEN = '3024233079-bWiNZu7wGUOQsakld8zIa2h19BhIVZGXmaTNi4e'
	OAUTH_TOKEN_SECRET = 'V4zLGMUuG7H2BwoThfxH9vpsMWjQDLRjgE60BIUGysGI3'
	auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
	twitter_api = twitter.Twitter(auth=auth)
	return twitter_api