#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy

bf = pd.read_table("~/qbb2015/stringtie/SRR072913/t_data.ctab")
bf2 = bf["FPKM"]>0



df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
df2 = df["FPKM"]>0


roi= df2 & bf2

bf3= bf[roi]["FPKM"]
df3= df[roi]["FPKM"]

df4=numpy.log(df3)
bf4=numpy.log(bf3)

M= bf4 - df4
A= 0.5 * (bf4 + df4)

#print M
#print A

plt.figure()
plt.plot(list(A), list(M), 'mo')
plt.title("MA Plot")
plt.xlabel("A")
plt.ylabel("M")
plt.savefig("MAplot.png")


