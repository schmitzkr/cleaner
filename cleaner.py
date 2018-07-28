#!/usr/bin/python -tt
f = open('dirt.txt','r+')
lines = f.readlines()
f.close()

g = open('dirt.txt', 'w')
list = []
for item in lines:
	s = str(item)
	i = s.index(" ")
	s = item[:i]
	list.append(s)

#a = ", ".join(str(list))
#str(a[i:i+19] for i in xrange(0,len(a),19))

a = [s[i:i+19] for i in xrange(0,len(list),19)]
b = ", ".join(a)
print()
g.close()

#print(list)