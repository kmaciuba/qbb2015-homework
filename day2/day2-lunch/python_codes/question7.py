#!/usr/bin/env python

filename= "/Users/cmdb/qbb2015/genomes/mappedReads"

f = open(filename)

count=0

for read in f:
    fields=read.split()
    if "@" not in fields[0]: 
        if fields[2]== "2L":
             if 10000<=int(fields[3])<=20000:
                 count+=1
            
print count