from django.db import models

class Main(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

class Tweet(models.Model):
    type = models.CharField(max_length = 300, default='type')
    text = models.CharField(max_length = 1000, default='text')
    name = models.CharField(max_length = 300, default='name')
    username = models.CharField(max_length = 300, default='username')
    location = models.CharField(max_length = 300, default='location')
    month = models.CharField(max_length = 10, default='month')
    hour = models.CharField(max_length = 300, default='hour')
    date = models.CharField(max_length = 300, default='day')
    day = models.CharField(max_length = 300, default='day')
    min =  models.CharField(max_length = 300, default='min')
    year =  models.CharField(max_length = 300, default='year')
    retweet =  models.CharField(max_length = 300, default='retweet')
    favorite =  models.CharField(max_length = 300, default='favorite')
    img =  models.TextField(max_length = 500, default='img')
    bg = models.TextField(max_length = 500, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.type)
