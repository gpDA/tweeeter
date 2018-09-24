def dateConvert(date):
    Rdata = ''
    if "Mon":
        Rdata = "Monday"
    elif "Tue":
        Rdata = "Tuesday"
    elif "Wed":
        Rdata = "Wednesday"
    elif "Thu":
        Rdata = "Thursday"
    elif "Fri":
        Rdata = "Friday"
    elif "Sat":
        Rdata = "Saturday"
    elif "Sun":
        Rdata = "Sunday"
    else:
        Rdata = "Undefined"
    
    return Rdata
        

def hourConvert(hour):
    INThour = int(hour)
    Rdata = ''
    if INThour == 24:
        Rdata = "00AM"
    elif INThour == 12:
        Rdata = "12PM"
    elif INThour > 12:
        Rdata = str((INThour - 12)) + "PM"
    else:
        if INThour > 9:
            Rdata = str(INThour) + "AM"
        else:
            Rdata = "0"+str(INThour) + "AM"
    
    return Rdata

        
        
        
        