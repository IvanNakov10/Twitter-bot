import tweepy
import keys
import requests
# Authenticate with Twitter using your consumer key and secret
auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
auth.set_access_token(keys.access, keys.access_secret)

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'symbol':'BTC,ETH,GALA',
  'convert':'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '634562be-a173-41d3-8c5d-e4229f52baea'
}

response = requests.get(url, headers=headers, params=parameters)

data = response.json()

btc_price = round(data['data']['BTC']['quote']['USD']['price'], 2)
eth_price = round(data['data']['ETH']['quote']['USD']['price'], 2)
gala_price = round(data['data']['GALA']['quote']['USD']['price'], 2)

# Create an API object
api = tweepy.API(auth)
btcpriceIvan = btc_price*0.001 
galaamount = gala_price*630.8
ethamount = eth_price*0.03
text = "your crypto is valued at: "
hole_amount = round(btcpriceIvan+galaamount+ethamount, 2)
allthing = text + str(hole_amount) + "$"
# Post a tweet
api.update_status(allthing)






