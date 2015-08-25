#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/USERS/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment='#', header= None)

df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attribute"]

#print df.head

roi= df["attribute"].str.contains("Sxl")

df2= df[roi]

roi2= df2["type"].str.contains("transcript")


plt.figure()
plt.plot(df2[roi2]["start"])
plt.title("Sxl transcripts")
plt.xlabel("Genes")
plt.ylabel("Start Position")
plt.savefig("Sxl_transcripts.png")


