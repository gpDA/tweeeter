from django.conf import settings
from django.shortcuts import render
import tweepy
from tweepy.auth import OAuthHandler
from . import handlingdata as hd

def TweetLive(request):
    auth = OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    
    api = tweepy.API(auth)
    
    print(settings.CONSUMER_KEY)
    print(settings.CONSUMER_SECRET)
    print(settings.ACCESS_TOKEN)
    print(settings.ACCESS_TOKEN_SECRET)

    #tweet_data = {}
    for status in tweepy.Cursor(api.search, q="#NYU", count=0, result_type="popular").items():
        json_data = (status._json)
        
        #popular_txt = json_data['text']
        #user.name
        #user.screen_name
        #created_at
        #retweet_count
        #favorite_count
        print('text',json_data['text'])
        print('user.name',json_data['user']['name'])
        print('user.name',json_data['user']['screen_name'])
        #print('user.screen_name',json_data.user['screen_name'])
        #print((json_data['created_at'].split(" ")))
        dta = (json_data['created_at'].split(" "))
        print(hd.dateConvert(dta[0])) #Thu
        print(dta[1]) #Sep
        print(dta[2]) #13 #day
        print(dta[3][0:2]) #14 hour
        print(dta[3][3:5]) #20 min
        print(dta[5]) #2018

        



        print('retweet_count',json_data['retweet_count'])
        print('favorite_count',json_data['favorite_count'])

    
    return render(request, 'frontend/index.html') 