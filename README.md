# hashtagNYU
Find out NYU in twitter ! I love my school and I find tweets with #NYU in many different filters 

#### Objective of this exercise 
 : is to practice with API contract for web development. I use Django (Python) for Backend and React.js for Frontend. 
 Also, request API and get the response is so important for the web development in todays. So I used twitter REST API to
 get tweets with #NYU. I request Twitter API using tweepy (provided for Django) in 3 different result_type 1) recent 2) popular 3) geocode (within 1 km away from Washington Square Park near NYU)
 
### VIDEO DEMO

[![hashtagNYU video Demo](https://img.youtube.com/vi/duJi753-YgE/2.jpg)](https://www.youtube.com/watch?v=xPcY2o0Yk8c)


### Run the Code

```
source ./bin/active
pip install -r requirements.txt  // PIP INSTALL EVERYTHING IN requirements.txt
npm run dev
cd project
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```





