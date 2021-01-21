#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#  The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they 
# appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop 
# to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts=dict()
for line in handle:
    if not line.startswith('From:'):
        continue
    words=line.split()
    counts[words[1]]=counts.get(words[1],0) + 1 #query value of the key , if not exist default to 0
print(counts)

bigName = None
bigValue = None
for n,v in counts.items():
    if bigName is None or v>bigValue:
        bigName=n
        bigValue=v
print(bigName,bigValue)