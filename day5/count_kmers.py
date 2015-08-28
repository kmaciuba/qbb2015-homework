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
            counts[kmer]=1
        else:
            counts[kmer]+=1

for key in sorted(counts, key=counts.get): #print keys/values in order of least to most frequent 
    print key, counts[key]
    
    
    