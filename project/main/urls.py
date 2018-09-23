from django.urls import path
from . import views

urlpatterns = [
    path('api/main/', views.MainListCreate.as_view() ),
    path('api/tweet/', views.TweetLive),
]