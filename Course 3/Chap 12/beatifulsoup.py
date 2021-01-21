#Get links href on a web page using beautiful soup

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read() #Return single big string with bunch of new lines, this is UTF-8
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all anchor tags
tags= soup('a') #Give list of anchor tags
for tag in tags:
    print(tag.get('href', None)) #None is default falue