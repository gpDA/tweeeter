from main.models import Main, Tweet
from main.serializers import TweetSerializer
from . import handlingdata as hd

from rest_framework.views import APIView
from rest_framework import permissions, viewsets
from django.http import JsonResponse
from django.conf import settings

import tweepy
from tweepy.auth import OAuthHandler

#from tweepy import Stream
#from tweepy.streaming import StreamListener


"""
STREAMING
class MyStreamListener(StreamListener):
    
    def on_status(self, status):
        #print(status)
        text = status._json['text']
        print(text)
        created_at = status._json['created_at']
        print(created_at)
        uname = status._json['user']['name']
        print(uname)
        usname = status._json['user']['screen_name']
        print(usname)
        uimg = status._json['user']['profile_image_url']
        print(uimg)        
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

#override tweepy.StreamListener to add logic to on_statusmyStreamListener = MyStreamListener()

myStream = Stream(auth, MyStreamListener())
myStream.filter(track=['#NYU'])
"""




"""
in class (method)
"""
'''
auth = OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

data = tweepy.Cursor(api.search, q='#NYU', geocode="40.72942,-73.99721,1km")
print(data)
'''



"""
1. frontend calls for backend; call tweepy
2. management command call to retrieve data

build own manage.py 
"""

"""
auth = OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
for statusNEAR in tweepy.Cursor(api.search, q='#NYU', geocode="40.72942,-73.99721,1km").items(1):
    json_dataNEAR = (statusNEAR._json)
    print(json_dataNEAR)
"""



class TweetView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        auth = OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
        auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True)

        dic = {}
        for statusNEAR in tweepy.Cursor(api.search, q='#NYU', geocode="40.72942,-73.99721,1km").items(1):
            json_dataNEAR = (statusNEAR._json)

            print()
            
            nearTEXT_data = json_dataNEAR['text']
            nearNAME_data = json_dataNEAR['user']['name']
            nearUSERNAME_data = json_dataNEAR['user']['screen_name']
            nearLOCATION_data = json_dataNEAR['user']['location']
            nearCREATED_data = (json_dataNEAR['created_at'].split(" "))
            nearMONTH_data = hd.dateConvert(nearCREATED_data[1])
            nearDAY_data = nearCREATED_data[2]
            nearHOUR_data = hd.hourConvert(nearCREATED_data[3][0:2])
            nearMIN_data = nearCREATED_data[3][3:5]
            nearYEAR_data = nearCREATED_data[5]
            nearRETWEET_data = json_dataNEAR['retweet_count'] #retweet_count
            nearFAVORITE_data = json_dataNEAR['favorite_count'] #favorite_count
            nearIMGURL_data = json_dataNEAR['user']['profile_image_url'] #    
        
            dic = {'type': 'near', 'text': nearTEXT_data, 'name': nearNAME_data,
                'username': nearUSERNAME_data, 'location': nearLOCATION_data, 'month': nearMONTH_data,
                'day': nearDAY_data, 'hour': nearHOUR_data, 'min': nearMIN_data, 'year': nearYEAR_data,
                'retweet': nearRETWEET_data, 'favorite': nearFAVORITE_data, 'img': nearIMGURL_data
                }
        

        """
        Tweet.objects.create(
            type = 'type', text = 'text', name = 'name',
            username = 'username', location = 'location', month = 'month',
            day = 'day', hour = 'hour', min = 'min',
            year = 'year', retweet = 'retweet', favorite = 'favorite',
            img = 'img'
        )
        """
        
        Tweet.objects.create(
            type = dic['type'], text = dic['text'], name = dic['name'],
            username = dic['username'], location = dic['location'], month = dic['month'],
            day = dic['day'], hour = dic['hour'], min = dic['min'],
            year = dic['year'], retweet = dic['retweet'], favorite = dic['favorite'],
            img = dic['img']
        )
        result = []
        result.append(dic)
        return JsonResponse(result)

    #Tweet.objects.create()

    #REST FRAMEWORK ; react calls api / 
    #frontend -> backend
    #frontend calling 
