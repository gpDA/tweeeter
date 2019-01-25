# hashtagNYU
Find out NYU in twitter ! I love my school and I find tweets with #NYU in many different filters 

#### Objective of this exercise 
 : is to practice with API contract for web development. I use Django (Python) for Backend and React.js for Frontend. 
 Also, request API and get the response is so important for the web development in todays. So I used twitter REST API to
 get tweets with #NYU. I request Twitter API using tweepy (provided for Django) in 3 different result_type 1) recent 2) popular 3) geocode (within 1 km away from Washington Square Park near NYU)
 
VIDEO DEMO :
[https://www.youtube.com/watch?v=xPcY2o0Yk8c]

SAMPLE IMAGE :
![SAMPLE IMAGE](https://user-images.githubusercontent.com/29666846/46186092-d9da6e80-c2aa-11e8-9232-74f9c0ea42af.png)

sample REACT
[https://github.com/gpDA/hashtagNYU/blob/069c806d57601b6be2a54058a9c51eba456e44a2/project/frontend/src/components/Main/TweetModal/TweetModal.js#L6-L25]

```
const TweetModal = ({ data }) =>{
    return (<Aux>
          {data.map(el => {
              //console.log(el);
            return (
    <div className="container"> 
            
            <div className="heading"></div>
            <header >
                
                <div className="bio" key={el.id}>
                    <img src={el.background} alt="background" className="bg"></img>
                </div>
                <div className="avatarcontainer">
                    <img src={el.img}  alt="avatar" className="avatar"></img>                    
                    <div className="hover">
                        <div className="icon-twitter"></div>                    
                    </div>
                </div>
            </header>
```

sample MODELS.PY
[https://github.com/gpDA/hashtagNYU/blob/069c806d57601b6be2a54058a9c51eba456e44a2/project/main/models.py#L9-L25]
```
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
```

sample VIEWS.PY
[https://github.com/gpDA/hashtagNYU/blob/069c806d57601b6be2a54058a9c51eba456e44a2/project/main/views.py#L5-L54]
```
def get(self, request, *args, **kwargs):
    auth = OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
...
dicREC = {'type': 'recent', 'text': recTEXT_data, 'name': recNAME_data,
    'username': recUSERNAME_data, 'location': recLOCATION_data, 'day': recDAY_data,
     'month': recMONTH_data, 'date': recDATE_data, 'hour': recHOUR_data, 'min': recMIN_data, 
     'year': recYEAR_data, 'retweet': recRETWEET_data, 'favorite': recFAVORITE_data, 
     'img': recIMGURL_data, 'background': recBGURL_data
    }
dic['recent'] = dicREC
```

TO RUN CODE
```
source ./bin/active
PIP INSTALL EVERYTHING IN requirements.txt
npm run dev
CD project
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```





