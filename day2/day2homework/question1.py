#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/USERS/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment='#', header= None)

df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attribute"]

roi= df["attribute"].str.contains("Sxl")

plt.figure()
plt.plot(df[roi]["start"])
plt.title("Sxl")
plt.xlabel("Genes")
plt.ylabel("Start Position")
plt.savefig("Sxl.png")
