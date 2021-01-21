"""
#Import score
import urllib.request, urllib.response, urllib.error
import re

url = input('Enter -')
if len(url)<1 : url ='http://py4e-data.dr-chuck.net/comments_1143873.html'
fhand = urllib.request.urlopen(url) #Like open command
counts=dict()
totalScore = 0
for line in fhand:
    if re.search('^<tr><td>.+([0-9]+).*',line.decode()):
        scoreInd = re.findall('[0-9]+', line.decode())
        totalScore=totalScore+int(scoreInd[0])
print(totalScore)
"""
#Get links href on a web page using beautiful soup

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url)<1 : url ='http://py4e-data.dr-chuck.net/comments_1143873.html'
html = urllib.request.urlopen(url, context=ctx).read() #Return single big string with bunch of new lines, this is UTF-8
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all anchor tags
tags= soup('span') #Give list of anchor tags
count = 0
total = 0
for tag in tags:
    total = total + int(tag.contents[0]) #Give value of content
    count = count + 1 
print("Count",count)
print("Sum",total)
