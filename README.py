# CODE2040
#Viviana Bermudez, CODE2040 API Challenge
from json import dumps, loads
from urllibb2 import urlopen, Request

#Received help from Google, stackoverflow for writing the timestamp function
#Received help from a friend on how to pull tokens and information from URLs


receiveList=[]        #list of information to be received from URLs
info = {'token':'YRGq5WDlur'}
url = 'http://challenge.code2040.org/api/getstring' 
myURLs = ['http://challenge.code2040.org/api/getstring',
          'http://challenge.code2040.org/api/haystack',
          'http://challenge.code2040.org/api/prefix',
          'http://challenge.code2040.org/api/time']
          
          
for x in range(4):
    request = Request(myURLs[i], data=dumps(info))
    receiveList.append(loads(urlopen(request).read())['result'])

def reverseString():
    """takes input string, s, and returns it reversed"""
    
    string = receiveList[0]         #retrieve string to be reversed
    revString = string[::-1]        #reverse string
    return revString
    
    
   
def needleInHaystack():
    """return index of needle in haystack"""
    needle =receiveList[1]['needle']
    haystack = receiveList[1]['haystack']
    
    return haystack.index(needle)
    

def prefixFinder():
    """return array containing only strings that don't start with 
    this prefix"""
    Result = []                             #empty list where strings will be added
    prefix = receiveList[2]['prefix']
    array = receiveList[2]['array']
    
    for string in array:
        if x.startswith(str(prefix), 0, len(prefix)) == True:
            Result += [string]
    
    return Result
        

import dateutil.parser                           #from stackoverflow.com
def addSeconds(interval, datestamp):
    """adds 'interval' seconds to date represented by datestamp"""
    datestamp = receiveList[3]['datestamp']
    interval = receiveList[3]['interval']
    
    date1= dateutil.parser.parse(datestamp)
    date= str(date1)
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    hour = int(date[11:13])
    minute = int(date[14:16])
    second = int(date[17:19])
    seconds = int(interval)
    
    second += seconds
    if second >= 60:
        second -= 60
        minute += 1
        if minute == 60:
            minute = 00
            hour += 1
            if hour == 24:
                hour = 00
                day += 1
                if day == 32:
                    if month == 01 or month == 03 or month == 05 or month == 07 or month == 08 or month == 10 or month == 12:
                        day = 01
                        month += 1
                        if month == 13:
                            month = 12
                            year +=  1
                if day == 31:
                    if month = 04 or month = 06 or month = 09 or month = 11:
                        day = 01
                        month += 1
                if day == 29:
                    if month == 02:
                        if year % 4 == 0:
                            if year % 100 != 0:
                                if year %400 == 0:
                                    day = 01
                                    month += 1
                                    
    return date
    
    
    
    
    
Functions = [reverseString(), needleInHaystack(), prefixFinder(), addSeconds()]    
SendURL = ['http://challenge.code2040.org/api/validatestring',
          'http://challenge.code2040.org/api/validateneedle',
          'http://challenge.code2040.org/api/validateprefix',
          'http://challenge.code2040.org/api/validatetime']   
SendKeys = ['string', 'needle', 'array', 'datestamp']

for x in range(4):
    send = {'token': 'YRGq5WDlur', SendKeys[x]:Functions[x]}
    Rqst = Request(SendURL[x], data=dumps(send))
    final = loads(urlopen(Rqst).read())['result']
    print final
    
     
      
 

                        
