import tweepy
import requests
from django.conf import settings

def fetch_tweets():
    auth = tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET)
    api = tweepy.API(auth)
    tweets = api.user_timeline(screen_name='@BirajGhora84749', count=10)
    return tweets

def fetch_facebook_posts(access_token):
    try:
        response = requests.get(
            f"https://graph.facebook.com/v15.0/me/posts",
            params={"access_token": access_token}
        )

        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", [])
            return posts
        else:
            return None
    except requests.exceptions.RequestException:
        return None
