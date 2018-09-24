
"""
def TweetLive(request):
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
        
    context['pop'] = {}
    for statusPOP in tweepy.Cursor(api.search, q="#NYU", result_type="popular").items(1):
        json_dataPOP = (statusPOP._json)
        
        popTEXT_data = json_dataPOP['text'] #text
        #print(popTEXT_data)
        popNAME_data = json_dataPOP['user']['name'] #user.name
        popUSERNAME_data = json_dataPOP['user']['screen_name'] #user.screen_name
        popLOCATION_data = json_dataPOP['user']['location']
        
        popCREATED_data = (json_dataPOP['created_at'].split(" ")) #created_at
        popMONTH_data = hd.dateConvert(popCREATED_data[1]) #month
        popDAY_data = popCREATED_data[2] #day
        popHOUR_data = hd.hourConvert(popCREATED_data[3][0:2]) #hour
        popMIN_data = popCREATED_data[3][3:5] #min
        popYEAR_data = popCREATED_data[5] #year
        popRETWEET_data = json_dataPOP['retweet_count'] #retweet_count
        popFAVORITE_data = json_dataPOP['favorite_count'] #favorite_count
        popIMGURL_data = json_dataPOP['user']['profile_image_url'] #

        context['pop']['text'] = popTEXT_data
        context['pop']['name'] = popNAME_data
        context['pop']['username'] = popUSERNAME_data
        context['pop']['location'] = popLOCATION_data
        context['pop']['month'] = popMONTH_data
        context['pop']['day'] = popDAY_data
        context['pop']['hour'] = popHOUR_data
        context['pop']['min'] = popMIN_data
        context['pop']['year'] = popYEAR_data
        context['pop']['retweet'] = popRETWEET_data
        context['pop']['favorite'] = popFAVORITE_data
        context['pop']['imgurl'] = popIMGURL_data
        

    context['tandon'] = {}
    #MY SCHOOL
    for statusTANDON in tweepy.Cursor(api.search, q="#NYUTandonMade", result_type="recent").items(1):
        json_dataTANDON = (statusTANDON._json)
        
        tandonTEXT_data = json_dataTANDON['text'] #text
        #print(popTEXT_data)
        tandonNAME_data = json_dataTANDON['user']['name'] #user.name
        tandonUSERNAME_data = json_dataTANDON['user']['screen_name'] #user.screen_name
        tandonLOCATION_data = json_dataTANDON['user']['location']
        
        tandonCREATED_data = (json_dataTANDON['created_at'].split(" ")) #created_at
        tandonMONTH_data = hd.dateConvert(tandonCREATED_data[1]) #month
        tandonDAY_data = tandonCREATED_data[2] #day
        tandonHOUR_data = hd.hourConvert(tandonCREATED_data[3][0:2]) #hour
        tandonMIN_data = tandonCREATED_data[3][3:5] #min
        tandonYEAR_data = tandonCREATED_data[5] #year
        tandonRETWEET_data = json_dataTANDON['retweet_count'] #retweet_count
        tandonFAVORITE_data = json_dataTANDON['favorite_count'] #favorite_count
        tandonIMGURL_data = json_dataTANDON['user']['profile_image_url'] #

        context['tandon']['text'] = tandonTEXT_data
        context['tandon']['name'] = tandonNAME_data
        context['tandon']['username'] = tandonUSERNAME_data
        context['tandon']['location'] = tandonLOCATION_data
        context['tandon']['month'] = tandonMONTH_data
        context['tandon']['day'] = tandonDAY_data
        context['tandon']['hour'] = tandonHOUR_data
        context['tandon']['min'] = tandonMIN_data
        context['tandon']['year'] = tandonYEAR_data
        context['tandon']['retweet'] = tandonRETWEET_data
        context['tandon']['favorite'] = tandonFAVORITE_data
        context['tandon']['imgurl'] = tandonIMGURL_data

    context['recent'] = {}
    #near by TANDON
    for statusRECENT in tweepy.Cursor(api.search, q='#NYU', result_type="recent").items(1):
        json_dataRECENT = (statusRECENT._json)
        
        recentTEXT_data = json_dataRECENT['text'] #text
        #print(popTEXT_data)
        recentNAME_data = json_dataRECENT['user']['name'] #user.name
        recentUSERNAME_data = json_dataRECENT['user']['screen_name'] #user.screen_name
        recentLOCATION_data = json_dataRECENT['user']['location']
        
        recentCREATED_data = (json_dataRECENT['created_at'].split(" ")) #created_at
        recentMONTH_data = hd.dateConvert(recentCREATED_data[1]) #month
        recentDAY_data = recentCREATED_data[2] #day
        recentHOUR_data = hd.hourConvert(recentCREATED_data[3][0:2]) #hour
        recentMIN_data = recentCREATED_data[3][3:5] #min
        recentYEAR_data = recentCREATED_data[5] #year
        recentRETWEET_data = json_dataRECENT['retweet_count'] #retweet_count
        recentFAVORITE_data = json_dataRECENT['favorite_count'] #favorite_count
        recentIMGURL_data = json_dataRECENT['user']['profile_image_url'] #        

        context['recent']['text'] = recentTEXT_data
        context['recent']['name'] = recentNAME_data
        context['recent']['username'] = recentUSERNAME_data
        context['recent']['location'] = recentLOCATION_data
        context['recent']['month'] = recentMONTH_data
        context['recent']['day'] = recentDAY_data
        context['tandon']['hour'] = recentHOUR_data
        context['recent']['min'] = recentMIN_data
        context['recent']['year'] = recentYEAR_data
        context['recent']['retweet'] = recentRETWEET_data
        context['recent']['favorite'] = recentFAVORITE_data
        context['recent']['imgurl'] = recentIMGURL_data

    print(context)
    return render(request, 'frontend/index.html', {'context': context})     
"""