import re

#re.search() return True or False based on matching regex
"""
hd = open("mbox-short.txt")
for line in hd:
    line = line.rstrip()
    #if re.search('From: ',line): #Match char From: from each line
    #    print(line)
    if re.search('^From: ',line): #mirip line.startswitch('From:')
        print(line)
 """

 #re.findall() if we want exactly the string we want
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x) # + means match 1 or more time
print(y) # will return list of found character ['2','19','42']

#Greedy means match longest possible.

#Get Email from log
x = "From stephen@gmail.com Sat Jan  5 21:12:01 2008"
print(re.findall('\S+@\S+',x)) #match non white-space character at lease once, followed by @, followed by non ws char at least once
print(re.findall('\S+@\S+?',x)) #if not greedy will match only stephen@g
print(re.findall('^From (\S+@\S+)',x)) #kurung will tell which string to be extracted. only extract the email, not the whole match
print(re.findall('@([^ ]*)',x)) #match email domain name.. dont include @, match all non blank chars
print(re.findall('^From.*@([^ ]*)',x)) #match if only start with From, extract domain name

#Spam confidence
hd = open("mbox-short.txt")
numlist = list()
for line in hd:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line) #if 0-9 and . match..
    if len(stuff)!=1 : continue
    num = float(stuff[0])
    numlist.append(num)
print("Maximum", max(numlist)) #Print max number of spam confidence

#Escape char: make special char behave like normal
x = 'We just received $10.00 for cookies'
y = re.findall('\$[0-9.]+',x) #dollar have special usage, to make it regular, use \
print(y)

x= 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+',x) #Even if ? exist in first \S , because it still need to match @, hostname will be fullmatched. 
print(y)