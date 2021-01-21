purse=dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
purse['candy'] = purse['candy'] + 2
print(purse)

##Counting occurence to dictionary
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name,0)+1 #Get value from key specified from dict, if not listed default is 0
print(counts)

#printing dictionary key and value
counts = {'chuck':1, 'fred':42, 'jan':100}
for key in counts:
    print(key,counts[key])

#Retrieve from dict to list key or value only
jjj = {'chuck':1, 'fred':42, 'jan':100}
print(list(jjj)) #convert to list(key only)
print(jjj.keys()) #return list of key only
print(jjj.values()) # return list of value only
print(jjj.items()) #Return list of (tuple constructed of value and key)

#return 2 variable from .items()
for k,v in jjj.items(): #get 2 variable aaa and bbb every loop of list of tuple
    print(k,v)

#reading from file and counting the name and find the most occured word
handle = open('romeo.txt')

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word]=counts.get(word,0) + 1
print(counts)

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count>bigcount: #bila iterasi pertama atau count>bigcount
        bigword=word
        bigcount=count

print("Most occured word: ",bigword," =",bigcount)