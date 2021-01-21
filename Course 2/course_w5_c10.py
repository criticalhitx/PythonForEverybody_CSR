#Tuple

x = ('Glenn', 'Sally', 'Joseph')
print(x[2]) #Joseph
y = (1,9,2)
print(y)
print(max(y))

for iter in y:
    print(iter)

#Tuple are immutable, cant alter like list. this is similar property to string
#Tuple cant be sorted, cant be appended
#Tuple more efficient in memory and processing, to make temp variable, prefer tuple over list

#Double assignment
(x, y) = (4, 'fred')
print(x)
print(y)

#Tuple is comparable
print((0,1,2)<(-2,5,6)) #False. Compare most significant item first

#Sort by key, 
d = {'a':10, 'c':1, 'b':22}
t = sorted(d.items())  #.items() return list of tuple #Sorting list
print(t)

#Sort by Value 
d = {'a':10, 'c':1, 'b':22}
tmp = list()
for k,v in d.items():
    tmp.append((v,k)) #make value first item of tuple  
print(sorted(tmp)) #sort [(1, 'c'), (10, 'a'), (22, 'b')]
print(sorted(tmp, reverse=True)) #Reverse sorting of list [(22, 'b'), (10, 'a'), (1, 'c')]

#Even shorter
d = {'a':10, 'c':1, 'b':22}
print(sorted([(v,k) for k,v in d.items()]))

