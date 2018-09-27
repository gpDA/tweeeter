from main.models import Main, Tweet
from main.serializers import TweetSerializer
from . import handlingdata as hd

from rest_framework.views import APIView
from rest_framework import permissions, viewsets
from django.http import JsonResponse
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

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
        result = []


        dicREC = {}
        for statusREC in tweepy.Cursor(api.search, q='#NYU', result_type='recent').items(1):
            json_dataREC = (statusREC._json)


            recTEXT_data = json_dataREC['text']
            recNAME_data = json_dataREC['user']['name']
            recUSERNAME_data = json_dataREC['user']['screen_name']
            recLOCATION_data = json_dataREC['user']['location']
            recCREATED_data = (json_dataREC['created_at'].split(" "))
            recDAY_data = hd.dateConvert(recCREATED_data[0])
            recMONTH_data = recCREATED_data[1]
            recDATE_data = recCREATED_data[2]
            recHOUR_data = hd.hourConvert(recCREATED_data[3][0:2])
            recMIN_data = recCREATED_data[3][3:5]
            recYEAR_data = recCREATED_data[5]
            recRETWEET_data = json_dataREC['retweet_count'] #retweet_count
            recFAVORITE_data = json_dataREC['favorite_count'] #favorite_count
            recIMGURL_data = json_dataREC['user']['profile_image_url'] #              
            recBGURL_data = json_dataREC['user']['profile_background_image_url'] #                            

            dicREC = {'type': 'recent', 'text': recTEXT_data, 'name': recNAME_data,
                'username': recUSERNAME_data, 'location': recLOCATION_data, 'day': recDAY_data,
                 'month': recMONTH_data, 'date': recDATE_data, 'hour': recHOUR_data, 'min': recMIN_data, 
                 'year': recYEAR_data, 'retweet': recRETWEET_data, 'favorite': recFAVORITE_data, 
                 'img': recIMGURL_data, 'bg': recBGURL_data
                }
        dic['recent'] = dicREC


        dicPOP = {}
        for statusPOP in tweepy.Cursor(api.search, q='#NYU', result_type='popular').items(1):
            json_dataPOP = (statusPOP._json)


            popTEXT_data = json_dataPOP['text']
            popNAME_data = json_dataPOP['user']['name']
            popUSERNAME_data = json_dataPOP['user']['screen_name']
            popLOCATION_data = json_dataPOP['user']['location']
            popCREATED_data = (json_dataPOP['created_at'].split(" "))
            popDAY_data = hd.dateConvert(popCREATED_data[0])
            popMONTH_data = popCREATED_data[1]
            popDATE_data = popCREATED_data[2]
            popHOUR_data = hd.hourConvert(popCREATED_data[3][0:2])
            popMIN_data = popCREATED_data[3][3:5]
            popYEAR_data = popCREATED_data[5]
            popRETWEET_data = json_dataPOP['retweet_count'] #retweet_count
            popFAVORITE_data = json_dataPOP['favorite_count'] #favorite_count
            popIMGURL_data = json_dataPOP['user']['profile_image_url'] #              
            popBGURL_data = json_dataPOP['user']['profile_background_image_url'] #                

            dicPOP = {'type': 'popular', 'text': popTEXT_data, 'name': popNAME_data,
                'username': popUSERNAME_data, 'location': popLOCATION_data, 'day': popDAY_data,
                 'month': popMONTH_data, 'date': popDATE_data, 'hour': popHOUR_data, 'min': popMIN_data, 
                 'year': popYEAR_data, 'retweet': popRETWEET_data, 'favorite': popFAVORITE_data, 
                 'img': popIMGURL_data, 'bg': popBGURL_data
                }
        dic['poular'] = dicPOP


        dicNEAR = {}
        for statusNEAR in tweepy.Cursor(api.search, q='#NYU', geocode="40.72942,-73.99721,1km").items(1):
            json_dataNEAR = (statusNEAR._json)
            
            nearTEXT_data = json_dataNEAR['text']
            nearNAME_data = json_dataNEAR['user']['name']
            nearUSERNAME_data = json_dataNEAR['user']['screen_name']
            nearLOCATION_data = json_dataNEAR['user']['location']
            nearCREATED_data = (json_dataNEAR['created_at'].split(" "))
            nearDAY_data = hd.dateConvert(nearCREATED_data[0])
            nearMONTH_data = nearCREATED_data[1]
            nearDATE_data = nearCREATED_data[2]
            nearHOUR_data = hd.hourConvert(nearCREATED_data[3][0:2])
            nearMIN_data = nearCREATED_data[3][3:5]
            nearYEAR_data = nearCREATED_data[5]
            nearRETWEET_data = json_dataNEAR['retweet_count'] #retweet_count
            nearFAVORITE_data = json_dataNEAR['favorite_count'] #favorite_count
            nearIMGURL_data = json_dataNEAR['user']['profile_image_url'] #    
            nearBGURL_data = json_dataNEAR['user']['profile_background_image_url'] #    
        
            dicNEAR = {'type': 'near', 'text': nearTEXT_data, 'name': nearNAME_data,
                'username': nearUSERNAME_data, 'location': nearLOCATION_data, 'day': nearDAY_data,
                 'month': nearMONTH_data, 'date': nearDATE_data, 'hour': nearHOUR_data, 'min': nearMIN_data, 
                 'year': nearYEAR_data, 'retweet': nearRETWEET_data, 'favorite': nearFAVORITE_data, 
                 'img': nearIMGURL_data, 'bg': nearBGURL_data
                }

        dic['near'] = dicNEAR

        try:
            for ko, v0 in dic.items():
                existsN = Tweet.objects.get(name=v0['name'])
                existsT = Tweet.objects.get(text=v0['text'])

            result.append(dicPOP)
            result.append(dicNEAR)
            result.append(dicREC)

            #exists = Tweet.objects.get(text=dic['text'])
            return JsonResponse(result, safe=False)

        except ObjectDoesNotExist:
            for ko, v0 in dic.items():
                Tweet.objects.create(
                type = v0['type'], text = v0['text'], name = v0['name'],
                username = v0['username'], location = v0['location'], day = v0['day'],
                month = v0['month'], date = v0['date'], hour = v0['hour'], min = v0['min'],
                year = v0['year'], retweet = v0['retweet'], favorite = v0['favorite'],
                img = v0['img'], bg = v0['bg']
                )
        
            result.append(dicPOP)
            result.append(dicNEAR)
            result.append(dicREC)
            return JsonResponse(result, safe=False)

    #Tweet.objects.create()

    #REST FRAMEWORK ; react calls api / 
    #frontend -> backend
    #frontend calling 
