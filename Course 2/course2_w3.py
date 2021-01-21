#Reading a text file and splitting into set for each lines
"""
#Cara 1
xfile = open('mbox.txt')
inp = xfile.read() #read into single file
inp = inp.split('\n') #split into set
print(inp)
"""
#Sorting line with start with xxx 
"""
xfile = open('mbox.txt')
for line in xfile:
    line = line.rstrip()
    if line.startswith('This'):
        print(line)
"""
#Skip until string ("From: ")
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not 'From:' in line:
        continue
    print(line)
