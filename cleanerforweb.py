#!/usr/bin/python -tt
f = open('dirt.txt','r+')
lines = f.readlines()
f.close()

g = open('dirt.txt', 'w')
for item in lines:
	s = str(item)
	i = s.index(" ")
	g.write(item[:i] + ", ")
g.close()