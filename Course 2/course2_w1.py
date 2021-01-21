"""
x="banana"
count=0
for item in x:
    if (item=="a"):
        count=count+1
print("Number of A =", count)
"""

"""
#Slicing
s="Monty Python"
print(s[0:4]) #From index 0 up to 4 but not include 4 (Mont)
print(s[6:7]) #From index 0 to 6, but not include 6 (P)
print(s[6:20]) #From index 6 to 20, but not include 20. (Python)
print(s[:2]) #From Start until index 2, but not including index 2 (Mo)
print(s[8:]) #From index 8 until end (thon)
print(s[:]) #All (Monty Python)

fruit = "banana"
if 'a' in fruit:
    print("Found!")
"""
"""
greet = 'Hello Bob'
print(greet.lower()) #Print all lower string (hello bob)
print(greet.upper()) #Print all upper string (HELLO BOB)
print(greet.capitalize()) #1st letter is upper, other is lower (Hello bob)
print(greet.replace('Bob','Jane')) #it will replace found string to other (Hello Jane)
print(greet.replace('o','x')) #Hellx Bxb
"""
#Find Function
"""
fruit="banana"
print(fruit.find('na')) #return index of found(2)
print(fruit.find('z')) #return -1 if not found
"""
#Stripping white space
greet = '    Hello Bob  '
print(greet.lstrip()) #(Hello Bob  )
print(greet.rstrip()) #(     Hello Bob)
print(greet.strip())  #(Hello Bob)

#Starts with
line = 'Please have a nice day'
print(line.startswith("Please")) #Return boolean true
print(line.startswith("p")) #Return boolean false

#Parsing log, Lets sey we want to parse hostname
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 08:21:22 2008' 
atpos = data.find('@') #parse @location
sppos = data.find(' ', atpos) #second parameter of find is "Find underscore position Start with position atpos"
host = data[atpos+1:sppos]
print(host)
