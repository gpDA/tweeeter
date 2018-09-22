from django.conf import settings
from django.shortcuts import render
import tweepy
from tweepy.auth import OAuthHandler

def TweetLive(request):
    auth = OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    
    api = tweepy.API(auth)
    
    print(settings.CONSUMER_KEY)
    print(settings.CONSUMER_SECRET)
    print(settings.ACCESS_TOKEN)
    print(settings.ACCESS_TOKEN_SECRET)

    for status in tweepy.Cursor(api.search, q="#nyu", count="1", result_type="popular").items():
        print(status)
    return render(request, 'frontend/index.html') 