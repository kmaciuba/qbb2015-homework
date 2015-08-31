#! /usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


Blast= open(sys.argv[1])
Score=[]
Evalue=[]

for data in Blast:
    fields=data.split()
    if float(fields[11])>0:
        score=np.log(float(fields[11]))
        Score.append(score)
    
    if float(fields[10])>0:
        evalue=np.log(float(fields[10]))
        Evalue.append(evalue)    





    
plt.figure()
plt.hist(list(Score), 200)
plt.xlabel('log Score')
plt.ylabel('Frequency')
plt.title('Alignment Scores')
#plt.xlim(0, 7)
plt.savefig("Score.png")

#print Evalue



plt.figure()
plt.hist( list(Evalue), 200)
plt.xlabel('log evalue')
plt.ylabel('Frequency')
plt.title('Evalue')
plt.xlim(-50, 10)
plt.savefig("Evalue.png")

'''

plt.figure()
plt.scatter(list(Score), list(Evalue))
plt.xlabel('log Score')
plt.ylabel('log evalue')
plt.title('Score vs Evalue')
plt.savefig("scorevsevalue.png")

'''