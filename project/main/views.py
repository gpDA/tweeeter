from main.models import Main
from main.serializers import MainSerializer
from rest_framework import generics
from django.conf import settings
from django.shortcuts import render
import tweepy
from tweepy.auth import OAuthHandler
from . import handlingdata as hd



class MainListCreate(generics.ListCreateAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer

def TweetLive(request):
    auth = OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    #tweet_data = {}
    for statusNEAR in tweepy.Cursor(api.search, q='#NYU', geocode="40.72942,-73.99721,1km").items(1):
        json_dataNEAR = (statusNEAR._json)
        
        nearTEXT_data = json_dataNEAR['text']
        nearNAME_data = json_dataNEAR['user']['name']
        nearUSERNAME_data = json_dataNEAR['user']['screen_name']
        nearLOCATION_data = json_dataNEAR['user']['location']
        

        nearCREATED_data = (json_dataNEAR['created_at'].split(" "))
        nearMONTH_data = nearCREATED_data[1]
        nearDAY_data = nearCREATED_data[2]
        nearHOUR_data = nearCREATED_data[3][0:2]
        nearMIN_data = nearCREATED_data[3][3:5]
        nearYEAR_data = nearCREATED_data[5]
        nearRETWEET_data = json_dataNEAR['retweet_count'] #retweet_count
        nearFAVORITE_data = json_dataNEAR['favorite_count'] #favorite_count
        nearIMGURL_data = json_dataNEAR['user']['profile_image_url'] #

        #print(nearTEXT_data)
        #print(nearNAME_data)
        #print(nearUSERNAME_data)
        #print(nearMONTH_data)
        #print(nearDAY_data)
        #print(nearHOUR_data)
        #print(nearMIN_data)
        #print(nearYEAR_data)
        #print(nearRETWEET_data)
        #print(nearFAVORITE_data)
        #print(nearIMGURL_data)
        
    for statusPOP in tweepy.Cursor(api.search, q="#NYU", result_type="popular").items(1):
        json_dataPOP = (statusPOP._json)
        
        popTEXT_data = json_dataPOP['text'] #text
        #print(popTEXT_data)
        popNAME_data = json_dataPOP['user']['name'] #user.name
        popUSERNAME_data = json_dataPOP['user']['screen_name'] #user.screen_name
        popLOCATION_data = json_dataPOP['user']['location']
        
        popCREATED_data = (json_dataPOP['created_at'].split(" ")) #created_at
        popMONTH_data = popCREATED_data[1] #month
        popDAY_data = popCREATED_data[2] #day
        popHOUR_data = popCREATED_data[3][0:2] #hour
        popMIN_data = popCREATED_data[3][3:5] #min
        popYEAR_data = popCREATED_data[5] #year
        popRETWEET_data = json_dataPOP['retweet_count'] #retweet_count
        popFAVORITE_data = json_dataPOP['favorite_count'] #favorite_count
        popIMGURL_data = json_dataPOP['user']['profile_image_url'] #

    #MY SCHOOL
    for statusTANDON in tweepy.Cursor(api.search, q="#NYUTandonMade", result_type="recent").items(1):
        json_dataTANDON = (statusTANDON._json)
        
        tandonTEXT_data = json_dataTANDON['text'] #text
        #print(popTEXT_data)
        tandonNAME_data = json_dataTANDON['user']['name'] #user.name
        tandonUSERNAME_data = json_dataTANDON['user']['screen_name'] #user.screen_name
        tandonLOCATION_data = json_dataTANDON['user']['location']
        
        tandonCREATED_data = (json_dataTANDON['created_at'].split(" ")) #created_at
        tandonMONTH_data = tandonCREATED_data[1] #month
        tandonDAY_data = tandonCREATED_data[2] #day
        tandonHOUR_data = tandonCREATED_data[3][0:2] #hour
        tandonMIN_data = tandonCREATED_data[3][3:5] #min
        tandonYEAR_data = tandonCREATED_data[5] #year
        tandonRETWEET_data = json_dataTANDON['retweet_count'] #retweet_count
        tandonFAVORITE_data = json_dataTANDON['favorite_count'] #favorite_count
        tandonIMGURL_data = json_dataTANDON['user']['profile_image_url'] #


    #near by TANDON
    for statusRECENT in tweepy.Cursor(api.search, q='#NYU', result_type="recent").items(1):
        json_dataRECENT = (statusRECENT._json)
        
        recentTEXT_data = json_dataRECENT['text'] #text
        #print(popTEXT_data)
        recentNAME_data = json_dataRECENT['user']['name'] #user.name
        recentUSERNAME_data = json_dataRECENT['user']['screen_name'] #user.screen_name
        recentLOCATION_data = json_dataRECENT['user']['location']
        
        recentCREATED_data = (json_dataRECENT['created_at'].split(" ")) #created_at
        recentMONTH_data = recentCREATED_data[1] #month
        recentDAY_data = recentCREATED_data[2] #day
        recentHOUR_data = recentCREATED_data[3][0:2] #hour
        recentMIN_data = recentCREATED_data[3][3:5] #min
        recentYEAR_data = recentCREATED_data[5] #year
        recentRETWEET_data = json_dataRECENT['retweet_count'] #retweet_count
        recentFAVORITE_data = json_dataRECENT['favorite_count'] #favorite_count
        recentIMGURL_data = json_dataRECENT['user']['profile_image_url'] #        



    context = {
        'near': {
            'text' : nearTEXT_data,
            'name' : nearNAME_data,
            'username' : nearUSERNAME_data,
            'location' : nearLOCATION_data,
            'month' : nearMONTH_data,
            'day' : nearDAY_data,
            'hour' : nearHOUR_data,
            'min' : nearMIN_data,
            'year' : nearYEAR_data,
            'retweet' : nearRETWEET_data,
            'favorite' : nearFAVORITE_data,
            'imgurl' : nearIMGURL_data
        },
        'pop': {
            'text' : popTEXT_data,
            'name' : popNAME_data,
            'username' : popUSERNAME_data,
            'location' : popLOCATION_data,
            'month' : popMONTH_data,
            'day' : popDAY_data,
            'hour' : popHOUR_data,
            'min' : popMIN_data,
            'year' : popYEAR_data,
            'retweet' : popRETWEET_data,
            'favorite' : popFAVORITE_data,
            'imgurl' : popIMGURL_data            
        },
        'tandon': {
            'text' : tandonTEXT_data,
            'name' : tandonNAME_data,
            'username' : tandonUSERNAME_data,
            'location' : tandonLOCATION_data,
            'month' : tandonMONTH_data,
            'day' : tandonDAY_data,
            'hour' : tandonHOUR_data,
            'min' : tandonMIN_data,
            'year' : tandonYEAR_data,
            'retweet' : tandonRETWEET_data,
            'favorite' : tandonFAVORITE_data,
            'imgurl' : tandonIMGURL_data            
        },
        'recent': {
            'text' : recentTEXT_data,
            'name' : recentNAME_data,
            'username' : recentUSERNAME_data,
            'location' : recentLOCATION_data,
            'month' : recentMONTH_data,
            'day' : recentDAY_data,
            'hour' : recentHOUR_data,
            'min' : recentMIN_data,
            'year' : recentYEAR_data,
            'retweet' : recentRETWEET_data,
            'favorite' : recentFAVORITE_data,
            'imgurl' : recentIMGURL_data            
        }                
    }


    return render(request, 'frontend/index.html', context)     