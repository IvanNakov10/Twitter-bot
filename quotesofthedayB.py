import keys
import requests
import tweepy
import schedule
import time 

def quote():

    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access, keys.access_secret)

    response = requests.get("https://quotes.rest/qod")  
    data = response.json()

    quote = data['contents']['quotes'][0]['quote']
    author = data['contents']['quotes'][0]['author']

    print("Quote: " + quote)
    print("Author: " + author)

    api = tweepy.API(auth)
    quoteD = "Quote: " + quote + "\n" + "Author: " + author
    api.update_status(quoteD)


schedule.every().hours.do(quote)


while True:
    schedule.run_pending()
    time.sleep(1)

