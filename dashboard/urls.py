from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('twitter/', views.twitter, name='twitter'),
    path('facebook/', views.facebook, name='facebook'),
    path('fetch_tweets/', views.fetch_tweets, name='fetch_tweets'),  
    path('fetch_facebook_posts/', views.fetch_facebook_posts, name='fetch_facebook_posts'), 
    path('tweet-bar-chart/', views.tweet_bar_chart, name='tweet_bar_chart'),
    path('facebook-bar-chart/', views.facebook_bar_chart, name='facebook_bar_chart'),
    path('tweet-list/', views.tweet_list, name='tweet_list'),
    path('create-tweet/', views.create_tweet, name='create_tweet'),
    path('facebook-post-list/', views.facebook_post_list, name='facebook_post_list'),
    path('create-facebook-post/', views.create_facebook_post, name='create_facebook_post'),
]