#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation="/USERS/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

df = pd.read_table(annotation)



df2= df["FPKM"] >0

df3= df["FPKM"][df2]

#print df3
        


#top= df2[0:11572]
#middle= df2[11572:23144]
#bottom= df2[23144:34718]

top= df3[0:3183]
middle= df3[3183:6366]
bottom= df3[6366:9549]


plt.figure()
plt.title("FPKM")
plt.boxplot([top, middle, bottom])
plt.xlabel("Location")
plt.ylabel("FPKM")
plt.savefig("FPKM.png")
