#Retreive XML from web, count #of data and its SUM

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url)<1 : url = 'http://py4e-data.dr-chuck.net/comments_1143875.xml'
html = urllib.request.urlopen(url, context=ctx)
data = html.read()

print('Retrieved', len(data), 'characters')
print(data.decode())

tree = ET.fromstring(data)
occ = tree.findall('.//count')
occurence = len(occ)
print('Count:',occurence)
number=0

lst = tree.findall('comments/comment')
print(len(lst))
for item in lst:
    x=item.find('count').text
    number = number + int(x)
print('Sum:', number)
