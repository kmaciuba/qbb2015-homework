#!/usr/bin/env python

"""
Count intersection of two BED files
"""
from __future__ import division
import numpy
import sys
import matplotlib.pyplot as plt
import matplotlib_venn
import scipy
import copy



def arrays_from_len_file( fname ):
    arrays={}
    for line in open( fname):
        fields = line.split()
        name = fields[0]
        size = int(fields[1])
        arrays[name]= numpy.zeros( size, dtype=bool ) # arrays is dictionary, right hand size is stored in dictionary to the key "name." numpy.zeros makes amounts of zeros equal to the length of the chromosome 
    return arrays

def set_bits_from_file(arrays, fname):
    arrays2=copy.deepcopy(arrays)
    for line in open(fname):
        fields= line.split()
        #Parse fields
        chrom = fields[0]
        start =int(fields[1])
        end= int(fields[2])
        arrays2 [ chrom ][start : end] = 1 #Gives array built for chromosome. Slices regions of genome that are sensitive to DNase (between start and end). Look up chrom in dictionary, specifically from start to end and assigns value of 1
    return arrays2
        

arr= arrays_from_len_file( sys.argv[1])

x=set_bits_from_file(arr, sys.argv[2])
x2=set_bits_from_file(arr, sys.argv[3])
x3=set_bits_from_file(arr, sys.argv[4])


total = 0
overlap123 = 0
overlap1 = 0
overlap2 = 0
overlap3 = 0
overlap12 =0
overlap23 = 0
overlap13 =0
       
        
for filename in sys.argv[2:]:
 
            
    for line in open(filename):
        fields= line.split()  
        chrom = fields[0]
        start =int(fields[1])
        end= int(fields[2]) 
    
     
        sl1 =  x[chrom][start:end].any()
        sl2 = x2[chrom][start:end].any()
        sl3 = x3[chrom][start:end].any()
        sl12 = x[chrom][start:end].any() & x2[chrom][start:end].any()
        sl13 = x[chrom][start:end].any() & x3[chrom][start:end].any()
        sl23 = x2[chrom][start:end].any() & x3[chrom][start:end].any()
        sl123 = x[chrom][start:end].any() & x2[chrom][start:end].any() & x3[chrom][start:end].any()
        
        total+=1
        if sl1==True and sl2==False and sl3==False:
            overlap1+=1
        if sl1==False and sl2==True and sl3==False:
            overlap2+=1
        if sl1==False and sl2==False and sl3==True:
            overlap3+=1
        if sl1==True and sl2==True and sl3==False:
            overlap12+=1
        if sl1==True and sl2==False and sl3==True:
            overlap13+=1
        if sl1==False and sl2==True and sl3==True:
            overlap23+=1
        if sl1==True and sl2==True and sl3==True:
            overlap123+=1
        

    #need some if elif statements 


        # if sl1 = x[chrom][start:end] ~x2[chrom][start:end] ~ x3[chrom][start:end]:
        #     overlap1 += sl1.any()
        #
        # elif sl2 = x2[chrom][start:end] ~x[chrom][start:end] ~x3[chrom][start:end]:
        #     overlap2 += sl2.any()
        #
        # elif sl3 = x3[chrom][start:end] ~x[chrom][start:end] ~x2[chrom][start:end]:
        #     overlap3 += sl3.any()
        #
        # elif sl12 = x[chrom][start:end] & x2[chrom][start:end] ~x3[chrom][start:end]:
        #     overlap12 += sl12.any()
        #
        # elif sl13 = x[chrom][start:end] & x3[chrom][start:end]~ x2[chrom][start:end]
        #     overlap13 += sl13.any()
        #
        # elif sl23 = x2[chrom][start:end] & x3[chrom][start:end]~x[chrom][start:end]:
        #     overlap23 += sl23.any()
        #
        # elif sl123 = x[chrom][start:end] & x2[chrom][start:end] & x3[chrom][start:end]:
        #     overlap123 += sl123.any()
        # else:
        #     total += 1
    
    '''
    
        total += 1
        overlap123 += sl123.any()
        overlap1 += sl1.any()
        overlap2 += sl2.any()
        overlap3 += sl3.any()
        overlap12 += sl12.any()
        overlap23 += sl23.any()
        overlap13 += sl13.any()
 
 
     
    print filename    
    print overlap1
    print overlap2
    print overlap3
    print overlap12
    print overlap13
    print overlap23
    print overlap123
    print total
    '''
        
        
        
#print total, overlap1, overlap2, overlap3, overlap12, overlap13, overlap23, overlap123
        
print overlap1, overlap2, overlap3, overlap12, overlap13, overlap23, overlap123, total 
        
        
plt.figure()
matplotlib_venn.venn3(subsets= (overlap1, overlap2, int(0.5*overlap12), overlap3, int(0.5*overlap13), int(0.5*overlap23), int(0.3333333333*overlap123)), set_labels = (sys.argv[2], sys.argv[3], sys.argv[4]))
plt.savefig("VennDiagram")
    