#! /usr/bin/env python
import sys

"""Count kmers in fasta file"""

from fasta import FASTAReader

reader= FASTAReader(sys.stdin)
counts={}

k=11

#find kmer of length k=11 (DNA sequence= length of 11)
for ident, sequence in reader:
    for i in range(0, len(sequence)-k):
        kmer= sequence[i:i+k]
        if kmer not in counts:  #adding to dictionary, increasing value
            counts[kmer]=[ (ident, i) ] #first time we see kmer, add position
        else:
            counts[kmer].append((ident,i)) #appends list, adds new position

query = sys.argv[1]

#get matches
for i in range(0, len(query)-k): 
    kmer= query[i:i+k]
    if kmer in counts:
        matches = counts[kmer]
        for pos in matches:
            print i, pos



    
    