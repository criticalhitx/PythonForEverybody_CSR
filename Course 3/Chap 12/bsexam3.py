import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Main Program
web = input('Enter - ')
count = input('Enter count: ')
count = int(count)
position = input('Enter position: ')
position = int(position)

def letsGo(url,position):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    temp=tags[position-1].get('href', None)
    return temp


if len(web)<1 : web ='http://py4e-data.dr-chuck.net/known_by_Tatiana.html'
for i in range (count):
    nextUrl=letsGo(web,position)
    web=nextUrl
    print(web)
nameResult = re.findall('_([^_]*?)\.html',web)
nameResult = nameResult[0]
print(nameResult)
