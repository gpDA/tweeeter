from django.urls import path
#from django.conf.urls import url
from . import views

urlpatterns = [
    path('api/tweet/', views.TweetView.as_view() ),
    #path('api/stream/', views.MyStreamListener.as_view() ),
]