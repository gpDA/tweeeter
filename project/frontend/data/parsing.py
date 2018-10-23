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

############################
############################

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

#print(language)

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

############################
############################

days={}


for schools in datum:
    sc = ddic[schools]
    for num in range(len(sc)):
        if num == 0:
            pass
        day = sc[num]['day']
        hour = sc[num]['hour']
        if day not in days:
            days[day] = {}
        if hour not in days[day]:
            days[day][hour] = 0
        elif hour in days[day]:
            days[day][hour] += 1
print(days)

"""
{
  'Fri': {
    '09': 14,
    '16': 25,
    '15': 38,
    '21': 17,
    '18': 9,
    '11': 11,
    '23': 15,
    '22': 16,
    '14': 1,
    '03': 9,
    '00': 16,
    '20': 15,
    '19': 11,
    '17': 27,
    '12': 12,
    '10': 8,
    '08': 22,
    '07': 9,
    '06': 10,
    '05': 8,
    '04': 12,
    '02': 12,
    '01': 10
  },
  'Thu': {
    '15': 30,
    '14': 16,
    '16': 56,
    '21': 11,
    '17': 13,
    '19': 40,
    '23': 16,
    '04': 13,
    '01': 23,
    '05': 26,
    '22': 11,
    '20': 30,
    '18': 21,
    '13': 23,
    '12': 25,
    '11': 20,
    '10': 28,
    '09': 24,
    '08': 16,
    '07': 39,
    '06': 17,
    '03': 21,
    '02': 12,
    '00': 3
  },
  'Tue': {
    '19': 17,
    '15': 4,
    '14': 8,
    '23': 32,
    '22': 60,
    '21': 80,
    '17': 18,
    '13': 4,
    '12': 2,
    '09': 5,
    '07': 1,
    '06': 1,
    '05': 5,
    '04': 7,
    '03': 6,
    '02': 3,
    '01': 1,
    '00': 6,
    '16': 5,
    '20': 22,
    '18': 10,
    '11': 2,
    '10': 0,
    '08': 0
  },
  'Sun': {
    '19': 4,
    '23': 2,
    '15': 7,
    '22': 4,
    '21': 0,
    '20': 11,
    '18': 12,
    '17': 6,
    '16': 5,
    '14': 4,
    '13': 4,
    '12': 4,
    '11': 6,
    '10': 4,
    '09': 4,
    '08': 7,
    '07': 3,
    '06': 4,
    '05': 3,
    '04': 0,
    '03': 2,
    '02': 2,
    '01': 6,
    '00': 1
  },
  'Sat': {
    '16': 16,
    '08': 6,
    '21': 9,
    '18': 12,
    '17': 12,
    '14': 7,
    '03': 2,
    '00': 15,
    '23': 4,
    '22': 1,
    '20': 13,
    '19': 12,
    '15': 12,
    '13': 5,
    '12': 4,
    '11': 10,
    '10': 7,
    '09': 8,
    '07': 6,
    '06': 1,
    '05': 4,
    '04': 5,
    '02': 4,
    '01': 8
  },
  'Wed': {
    '22': 21,
    '21': 26,
    '17': 7,
    '02': 57,
    '01': 52,
    '00': 41,
    '20': 34,
    '14': 89,
    '23': 18,
    '19': 99,
    '18': 92,
    '16': 74,
    '15': 24,
    '13': 10,
    '12': 80,
    '11': 18,
    '10': 71,
    '09': 27,
    '08': 79,
    '07': 19,
    '06': 80,
    '05': 18,
    '04': 52,
    '03': 46
  },
  'Mon': {
    '23': 7,
    '22': 5,
    '21': 2,
    '20': 3,
    '19': 10,
    '18': 13,
    '13': 4,
    '14': 6,
    '17': 7,
    '16': 10,
    '15': 5,
    '12': 4,
    '11': 3,
    '10': 2,
    '09': 4,
    '08': 1,
    '07': 0,
    '06': 0,
    '05': 0,
    '04': 0,
    '03': 0,
    '02': 8,
    '01': 4,
    '00': 5
  }
}
"""