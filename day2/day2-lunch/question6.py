#!/usr/bin/env python

filename= "/Users/cmdb/qbb2015/genomes/mappedReads"

f = open(filename)
count=0 # #of lines
mapq=0 # total mapqs

for data in  f:
    field = data.split() #make some columns
    #MAPQ = field[4]
    if "@" not in field[0]: #no header
        mapq = mapq + int(field[4])
         #why doesn't using MAPQ in place of field[4] work?
        count+=1
        
print mapq/count
    
