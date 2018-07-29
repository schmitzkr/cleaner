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

t = [list[i:i + 20] for i in xrange(0, len(list), 20)]
	

print('\n'.join(map(str, t)))

g.close()

