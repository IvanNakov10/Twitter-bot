import tweepy
import keys
import requests
# Authenticate with Twitter using your consumer key and secret
auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
auth.set_access_token(keys.access, keys.access_secret)

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'symbol':'BTC',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '634562be-a173-41d3-8c5d-e4229f52baea'
}

response = requests.get(url, headers=headers, params=parameters)

data = response.json()
price = data['data']['BTC']['quote']['USD']['price']

# Create an API object
api = tweepy.API(auth)

# Post a tweet
api.update_status(price)






