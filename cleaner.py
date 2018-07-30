#!/usr/bin/python -tt
f = open('dirt.txt','r+')
lines = f.readlines()
f.close()

#g = open('dirt.txt', 'w')
unames = []

for item in lines:
	s = item
	i = s.index(" ")
	s = item[:i]
	unames.append(s)
	
v = [unames[i:i + 1] for i in xrange(0, len(unames), 1)]

#pr i in t:
for i in v:
	print [''.join(x) for x in unames]

#print t

#g.write(t)
#g.close()