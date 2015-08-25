#!/usr/bin/env python

filename= "/Users/cmdb/qbb2015/genomes/mappedReads"

f = open( filename )

alignments = {}

for line_count, data in enumerate( f ):
    fields = data.split()
    if not "@" in fields [0]:
       if fields[2] not in alignments:
            alignments [ fields[2] ] = 1
       else:
            alignments [fields[2]] += 1
    
 

#Iterate key, value pairs from name counts dictionary
for key in ["2L", "2R", "3L", "3R", "4", "X"]:
    print key, alignments[key]