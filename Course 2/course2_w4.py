#Slicing list
t=[9,41,12,3,74,15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

#Build list from scratch
stuff=list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)   

#sort list
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)

#list of number
nums = [3,41,12,9,74,15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

#double split
line = "From stephen.hawking@ac.dz.id Sat Jan  4 09:11:20 2008"
words = line.split()
email = words[1]
pieces = email.split('@')
domain = pieces[1]
print(domain)
