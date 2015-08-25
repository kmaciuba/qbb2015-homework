#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation="/USERS/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

df = pd.read_table(annotation)

df2= df["FPKM"]

top= df2[0:11572]
middle= df2[11572:23144]
bottom= df2[23144:34718]

plt.figure()
plt.title("FPKM")
plt.boxplot([top,middle,bottom])
plt.xlabel("Location")
plt.ylabel("FPKM")
plt.savefig("FPKM.png")
