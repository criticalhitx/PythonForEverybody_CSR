import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+12345678"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data) #parse json into dict
print(info)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

#as nested list and dictionary
input = '''[
    { "id" : "001",
      "x"  : "2",
      "name" : "Chuck"
    },
    { "id" : "009",
      "x"  : "7",
      "name" : "Suck"
    }
]'''

info = json.loads(input) #parse json into list of dict
print(info)
print('User count:', len(info)) #2
for item in info:
    print('Name:',item['name'])
    print('Id:',item['id'])
    print('Attribute:', item['x'])