#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy

df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
df2 = df[df["FPKM"]>0]

df3=numpy.log(df2["FPKM"])

#print df3

mu= numpy.mean(df3)
sigma= numpy.std(df3)
#print mu, sigma
x= mu+ sigma *numpy.random.randn(1000)
x.sort()

plt.figure()
plt.hist(list(df3))
y= mlab.normpdf(x, mu,sigma)
plt.plot(x,y*len(df3),"r--")



plt.xlabel("log FPKM")
plt.ylabel("frequency")
plt.title("Kernel density")
plt.savefig("kernel.png")
