import sys

i = open("entry.txt","r")
o = open("exit.txt","w")

xs = i.readlines()
l = len(xs)

for p in range(l):
    o.write(xs[l-p-1])

o.close()
i.close()