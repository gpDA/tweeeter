from django.db import models

class Main(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

class Tweet(models.Model):
    type = models.CharField(max_length = 300)
    text = models.CharField(max_length = 1000)
    name = models.CharField(max_length = 300)
    username = models.CharField(max_length = 300)
    location = models.CharField(max_length = 300)
    month = models.CharField(max_length = 10)
    day = models.IntegerField()
    min =  models.IntegerField()
    year =  models.IntegerField()
    retweet =  models.IntegerField()
    favorite =  models.IntegerField()
    img =  models.TextField(max_length = 500)


