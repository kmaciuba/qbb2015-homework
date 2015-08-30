#!/usr/bin/env python

from __future__ import division
import numpy
import sys
import matplotlib.pyplot as plt
import matplotlib_venn
import scipy
import copy
import chrombitsHOMEWORK

arr = chrombitsHOMEWORK.ChromosomeLocationBitArrays( fname=sys.argv[1] )


beaf= arr.copy()
ctcf= arr.copy()
suhw= arr.copy()

ctcf.set_bits_from_file(fname= sys.argv[2] )
beaf.set_bits_from_file(fname= sys.argv[3] )
suhw.set_bits_from_file(fname= sys.argv[4] )

union = ctcf.union( beaf.union(suhw) )




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
    
     
        sl1 =  ctcf.arrays[chrom][start:end].any()
        sl2 = beaf.arrays[chrom][start:end].any()
        sl3 = suhw.arrays[chrom][start:end].any()
        sl12 = ctcf.arrays[chrom][start:end].any() & beaf.arrays[chrom][start:end].any()
        sl13 = ctcf.arrays[chrom][start:end].any() & suhw.arrays[chrom][start:end].any()
        sl23 = beaf.arrays[chrom][start:end].any() & suhw.arrays[chrom][start:end].any()
        sl123 = ctcf.arrays[chrom][start:end].any() & beaf.arrays[chrom][start:end].any() & suhw.arrays[chrom][start:end].any()
        
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
        
        
    
        
print overlap1, overlap2, overlap3, overlap12, overlap13, overlap23, overlap123, total 
print union
        
plt.figure()
matplotlib_venn.venn3(subsets= (overlap1, overlap2, int(0.5*overlap12), overlap3, int(0.5*overlap13), int(0.5*overlap23), int(0.3333333333*overlap123)), set_labels = (sys.argv[2], sys.argv[3], sys.argv[4]))
plt.savefig("VennDiagram2.png")