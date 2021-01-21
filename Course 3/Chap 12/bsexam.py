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