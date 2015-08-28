#! /usr/bin/env python

import sys

Blast= open(sys.argv[1])

for line in Blast:
    
    if line.startswith("> NM_"):
        name= line.rstrip()
        print name,
        
    if line.startswith(" Identities"):
        column= line.split()
        iratio= column[2]
        print iratio, 
        
    if line.startswith(" Identities"):
        column= line.split()
        gratio= column[6]
        print gratio
     
#print name, iratio, gratio