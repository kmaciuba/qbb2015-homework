#!/usr/bin/env python

filename= "/Users/cmdb/qbb2015/genomes/mappedReads"

f = open(filename)

count=0

for line in f:
    field= line.split()
    if "@" not in field[0]:
        count += 1
print count,