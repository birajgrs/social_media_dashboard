import tweepy
import requests
from django.conf import settings
from django.shortcuts import render, HttpResponse
from .models import Tweet, FacebookPost

def index(request):
    return HttpResponse("Hello World!")

def twitter(request):
    tweets = Tweet.objects.all()
    return render(request, 'twitter.html', {'tweets': tweets})

def facebook(request):
    posts = FacebookPost.objects.all()
    return render(request, 'facebook.html', {'posts': posts})

def fetch_tweets(request):
    try:
        auth = tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET)
        auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

        api = tweepy.API(auth)
        tweets = api.user_timeline(screen_name='BirajGhora84749', count=10)

        for tweet in tweets:
            Tweet.objects.create(
                text=tweet.text,
                created_at=tweet.created_at,
                user=tweet.user.screen_name
            )
        return HttpResponse("Tweets fetched and saved successfully.")
    except tweepy.TweepError as e:
        return HttpResponse(f"Error fetching tweets: {str(e)}", status=500)

def fetch_facebook_posts(request):
    try:
        params = {
            'access_token': settings.FACEBOOK_ACCESS_TOKEN,
            'fields': 'message,created_time,from',
            'limit': 10  # Fetch the last 10 posts
        }

        response = requests.get('https://graph.facebook.com/v13.0/me/feed', params=params)
        data = response.json()

        for post_data in data.get('data', []):
            FacebookPost.objects.create(
                message=post_data.get('message', ''),
                created_time=post_data.get('created_time', ''),
                user_id=post_data.get('from', {}).get('id', '')
            )
        return HttpResponse("Facebook posts fetched and saved successfully.")
    except Exception as e:
        return HttpResponse(f"Error fetching Facebook posts: {str(e)}", status=500)
