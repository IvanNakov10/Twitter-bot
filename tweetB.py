import tweepy
import keys
import requests
import schedule
import time

def getPrices():
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

  # Authenticate with Twitter using your consumer key and secret

  btc_price = round(data['data']['BTC']['quote']['USD']['price'], 2)
  eth_price = round(data['data']['ETH']['quote']['USD']['price'], 2)
  gala_price = round(data['data']['GALA']['quote']['USD']['price'], 4)

  # Create an API object
  api = tweepy.API(auth)
  btcpriceIvan = btc_price*0.001 
  galaamount = gala_price*630.8
  ethamount = eth_price*0.03
  hole_amount = round(btcpriceIvan+galaamount+ethamount, 2)

  cryptotoday = "Btc: " + str(btc_price) + "\n" + "Eth: " + str(eth_price) + "\n" + "Gala: " + str(gala_price) +"\n" + "\n" "Your crypto is valued at: " + str(hole_amount) + "$"
  # Post a tweet
  api.update_status(cryptotoday)

schedule.every().hour.do(getPrices)


while True:
    schedule.run_pending()
    time.sleep(1)





