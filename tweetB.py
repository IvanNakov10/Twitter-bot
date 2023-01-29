import tweepy
import keys

# Authenticate with Twitter using your consumer key and secret
auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
auth.set_access_token(keys.access, keys.access_secret)

# Create an API object
api = tweepy.API(auth)

# Post a tweet
api.update_status("btc up")