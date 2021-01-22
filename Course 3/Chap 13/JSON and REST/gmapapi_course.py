import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
api_key = 'zaSyDXOG1q2gOZxNv1Vb8ho2zH4SLuM38J9o0' # Not Real One.. 

while True:
    address = input('Enter Location: ')
    if len(address) < 1 : break
    url = serviceurl + urllib.parse.urlencode({'address': address, 'key': api_key})
    
    print('Retreiving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None
    
   # print(data)
   
    if not js or 'status' not in js or js['status']!= 'OK':
        print('====Failure to retreive===')
        #print(data)
        continue
    
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat',lat,'lng',lng)
    location = js['results'][0]['formatted_address']
    print(location)