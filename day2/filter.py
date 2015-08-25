#!/usr/bin/env python

filename= "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open( filename )

for line in f:
    fields = line.split()
    if "tRNA" in fields[9]:
        print line,

