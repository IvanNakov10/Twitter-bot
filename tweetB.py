import tweepy
import keys
def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access, keys.access_secret)

    return tweepy.API(auth)

def tweet(api: tweepy.API, message:str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print('Done')

if __name__ == '__name__':
    api = api()
    tweet(api, 'This was tweeted by a bot!', 'photos\light1.png')

