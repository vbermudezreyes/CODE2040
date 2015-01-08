# CODE2040
#Viviana Bermudez, CODE2040 API Challenge
from json import dumps, loads
from urllib2 import urlopen, Request

#Received help from Google, stackoverflow for writing the timestamp function
#Received help from a friend on how to pull tokens and information from URLs


receiveList=[]        #list of information to be received from URLs
info = {'token':'YRGq5WDlur'}
 
myURLs = ['http://challenge.code2040.org/api/getstring',
          'http://challenge.code2040.org/api/haystack',
          'http://challenge.code2040.org/api/prefix',
          'http://challenge.code2040.org/api/time']
          
          
for x in range(4):
    print "inject 1"
    request = Request(myURLs[x], data=dumps(info))
    print "inject 2"
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
        if string.startswith(str(prefix), 0, len(prefix)) == False:
            Result += [string]
    
    return Result
        

    
import datetime
def addInterval():
    date = receiveList[3]['datestamp']
    numSecs = receiveList[3]['interval']
    initialTime = datetime.datetime(int(date[0:4]),
    int(date[5:7]),
    int(date[8:10]),
    int(date[11:13]),
    int(date[14:16]),
    int(date[17:19]),
    int(date[20:23]))
    
    print initialTime
    
    finalTime = initialTime + datetime.timedelta(seconds=numSecs)

    return finalTime.isoformat()
    
    
    
    
    
    
Functions = [reverseString(), needleInHaystack(), prefixFinder(), addInterval()]    
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
    
      
 

                        
