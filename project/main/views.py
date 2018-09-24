from main.models import Main, Tweet
from main.serializers import MainSerializer, TweetSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import render
import tweepy
from tweepy.auth import OAuthHandler
from . import handlingdata as hd

auth = OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

context = {}
context['near'] = {}
for statusNEAR in tweepy.Cursor(api.search, q='#NYU', geocode="40.72942,-73.99721,1km").items(1):
    json_dataNEAR = (statusNEAR._json)
    
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

    context['near']['text'] = nearTEXT_data
    context['near']['name'] = nearNAME_data
    context['near']['username'] = nearUSERNAME_data
    context['near']['location'] = nearLOCATION_data
    context['near']['month'] = nearMONTH_data
    context['near']['day'] = nearDAY_data
    context['near']['hour'] = nearHOUR_data
    context['near']['min'] = nearMIN_data
    context['near']['year'] = nearYEAR_data
    context['near']['retweet'] = nearRETWEET_data
    context['near']['favorite'] = nearFAVORITE_data
    context['near']['imgurl'] = nearIMGURL_data    

class MainListCreate(generics.ListCreateAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer

class TweetListCreate(generics.ListCreateAPIView):
    model = Tweet

    def get_serializer(self):
        return TweetSerializer
    
    def get_queryset(self):
        return Tweet.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.DATA)

        

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            tweet = Tweet.objects.create(
                type= 'near',
                text = context['near']['text'],
                name = context['near']['name'],
                username = context['near']['username'],
                location = context['near']['location'],
                
                month = context['near']['month'],
                day = context['near']['day'],
                hour = context['near']['hour'],
                min = context['near']['min'],
                year = context['near']['year'],
                retweet = context['near']['retweet'],
                favorite = context['near']['favorite'],
                img = context['near']['imgurl']
        )
        result = TweetSerializer(tweet)
        return Response(result.data, status=status.HTTP_201_CREATED)

    
