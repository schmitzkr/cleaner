#!/usr/bin/python -tt
f = open('dirt.txt','r+')
lines = f.readlines()
f.close()

g = open('dirt.txt', 'w')
unames = []

for item in lines:
	s = item
	i = s.index(" ")
	s = item[:i]
	unames.append(s)

for i in range(len(unames)/20+1):
    print ", ".join(unames[i*20:(i+1)*20]) + "\n"
	
# for i in range(len(unames)/20+1):
# 	g.write(", ".join(unames[i*20:(i+1)*20]) + "\n")

#g.close()