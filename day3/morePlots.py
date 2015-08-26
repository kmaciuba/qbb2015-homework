#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")

#FPKM vs developmental stage for females
Sxl_f= []
for sample in metadata[metadata["sex"] == "female"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/"+sample+"/t_data.ctab")
    roi = df ["t_name"].str.contains("FBtr0331261")
    Sxl.append(df[roi]["FPKM"].values)
    
    
    
Sxl_m= []
for sample in metadata[metadata["sex"] == "male"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/"+sample+"/t_data.ctab")
    roi = df ["t_name"].str.contains("FBtr0331261")
    Sxl.append(df[roi]["FPKM"].values)
    
    
plt.figure()
plt.plot(Sxl_f)
plt.plot(Sxl_m)
plt.savefig("timecourse.png")







df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
df2 = pd.read_table("~/qbb2015/stringtie/SRR072915/t_data.ctab")

plt.figure() #scatterplot, 915 vs 893
plt.scatter(df["FPKM"], df2["FPKM"])
plt.xlabel("893 - male 10")
plt.ylabel("915 - female 14D")
plt.savefig("scatterplot.png")





chromosomes = {}

for i, line in df.iterrows():
    if line["chr"] in ["2L", "2R", "3L", "3R", "X", "Y"]:
        if line["chr"] not in chromosomes:
            chromosomes[line["chr"]] = 1 #first time we see it
        else:
            chromosomes[line["chr"]] += 1 # adds 1 for multiples

#print range(len(chromosomes))) get number of xs 
#chromosomes.values() get values from dict, height (y value)
#print chromosomes.keys() get keys from dict

plt.figure()
plt.bar(range(len(chromosomes)), chromosomes.values()) #(x,y)
plt.xticks(range(len(chromosomes)), chromosomes.keys()) #adds labels to categories on x value
plt.savefig ("barplot.png")
