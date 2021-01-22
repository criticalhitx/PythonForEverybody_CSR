import urllib.request, urllib.parse, urllib.error
import json


url = input('Enter Location:')
if len(url)<1 : url = 'http://py4e-data.dr-chuck.net/comments_1143876.json'
print('Retreiving', url)

uh = urllib.request.urlopen(url)
data = uh.read().decode() #Json string
js = json.loads(data) #dict


x=js['comments']
print(x)
summ = 0
count = 0 
for i in x:
    inscore = i['count'] #Individual Score
    summ = summ + inscore
    count = count + 1
print ('Count:', count)
print ('Sum:', summ)