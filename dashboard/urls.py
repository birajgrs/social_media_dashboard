from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('twitter/', views.twitter, name='twitter'),
    path('facebook/', views.facebook, name='facebook'),
    path('fetch_tweets/', views.fetch_tweets, name='fetch_tweets'),  
    path('fetch_facebook_posts/', views.fetch_facebook_posts, name='fetch_facebook_posts'),  
]
