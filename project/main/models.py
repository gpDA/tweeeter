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
    #django.db.utils.IntegrityError: NOT NULL constraint failed: main_tweet.background
    background = models.URLField(max_length = 500, null=True, default='https://www.cbronline.com/wp-content/uploads/2016/06/twitter2.png')
    img =  models.URLField(max_length = 500, default='https://yt3.ggpht.com/a-/AN66SAyn4D2lHHaONid5n_y_ZIsyInEUOoktizKFew=s900-mo-c-c0xffffffff-rj-k-no')
    
    

    def __str__(self):
        return "{}".format(self.type)
