import data

#print(data.dic)
ddic = data.dic

datum = list(ddic.keys())

#for schools in datum:
#    print(schools, len(ddic[schools]))

#wagner 6
#tisch 4
#stern 59
#steinhardt 10
#sps 3
#silver 2
#shanghai 0
#schoolofmed 1
#publichealth 0
#nursing 0
#law 38
#gallatin 1
#ifa 0
#dental 0
#courant 0
#cas 0
#abudhabi 1
#isaw 0
#nyu 2727    

language={}

for schools in datum:
    sc = ddic[schools]
    for num in range(len(sc)):
        if num == 0:
            pass
        lang = sc[num]['lang']
        if lang not in language:
            language[lang] = 0
        language[lang] += 1

print(language)

#{'en': 1649, ENGLISH 
# 'nl': 1,  DUTCH
# 'es': 14, SPANISH
# 'en-gb': 41, ENGLISH?
# 'ru': 838, RUSSIAN
# 'tr': 96, TURKISH
# 'pt': 4, PORTUGUESE
# 'id': 115, INDONESIAN
# 'ja': 3, JAPANESE
# 'th': 3, THAI
# 'it': 12, ITLIAN
# 'ar': 5, ARABIC
# 'fr': 11, FRENCH
# 'pl': 1, POLISH 
# 'uk': 35, UKRANIAN
# 'vi': 11, VIETNAMESE
# 'zh-cn': 1, CHINESE
# 'de': 4, GERMAN
# 'ro': 2, ROMANIAN
# 'bg': 1, ?UNKONWN
# 'hu': 1, HUNGARIAN
# 'cs': 1, CZECH
# 'hr': 2, ?UNKNOWN
# 'en-GB': 1 ENGLISH?
# }


#print(ddic['wagner'][0]['lang'])