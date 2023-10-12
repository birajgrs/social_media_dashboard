from django.shortcuts import render, redirect
from .models import Tweet, FacebookPost
from .forms import TweetForm, FacebookPostForm
import tweepy
import requests
from django.conf import settings
from django.http import HttpResponse
import matplotlib.pyplot as plt

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
        auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)

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

def tweet_bar_chart(request):
    tweets = Tweet.objects.all()
    tweet_dates = [tweet.created_at for tweet in tweets]
    tweet_counts = [len(tweets)]
    plt.bar(tweet_dates, tweet_counts)
    plt.title('Tweet Counts Over Time')
    plt.xlabel('Date')
    plt.ylabel('Tweet Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('tweet_chart.png')
    
    return render(request, 'tweet_bar_chart.html')

def facebook_bar_chart(request):
    posts = FacebookPost.objects.all()
    post_dates = [post.created_time for post in posts]
    post_counts = [len(posts)]
    plt.bar(post_dates, post_counts)
    plt.title('Facebook Post Counts Over Time')
    plt.xlabel('Date')
    plt.ylabel('Post Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('facebook_chart.png')
    
    return render(request, 'facebook_bar_chart.html')

def tweet_list(request):
    tweets = Tweet.objects.all()
    return render(request, 'tweet_list.html', {'tweets': tweets})

# View to create a new tweet
def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')  # Redirect to the tweet list
    else:
        form = TweetForm()
    return render(request, 'create_tweet.html', {'form': form})

# View to list Facebook posts
def facebook_post_list(request):
    facebook_posts = FacebookPost.objects.all()
    return render(request, 'facebook_post_list.html', {'facebook_posts': facebook_posts})

# View to create a new Facebook post
def create_facebook_post(request):
    if request.method == 'POST':
        form = FacebookPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facebook_post_list')  # Redirect to the Facebook post list
    else:
        form = FacebookPostForm()
    return render(request, 'create_facebook_post.html', {'form': form})
