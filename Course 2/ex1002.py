#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each
#  of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string 
# a second time using a colon.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    splitted=line.split()
    x= len(splitted)-2 #Time index
    time = splitted[x] #Get Time
    temp = time.split(':')
    hour = temp[0] # get hour only
    dic[hour]=dic.get(hour,0)+1 #Counter to dict
print(dic)
sortedlist=sorted(dic.items()) #Create sorted list of tuples from dic
for hour,occurence in sortedlist: #get 2 variable from sorted list of tuple
    print(hour,occurence)