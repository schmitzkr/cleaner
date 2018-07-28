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

a = str(", ".join(list))
g.write(a[i:i+19] for i in xrange(0,len(a),19))

g.close()
#print(list)