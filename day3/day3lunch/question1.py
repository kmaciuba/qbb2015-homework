#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")
replicates = pd.read_csv("/Users/cmdb/qbb2015/rawdata/replicates.csv")

Sxl_f= []
for sample in metadata[metadata["sex"] == "female"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/"+sample+"/t_data.ctab")
    roi = df ["t_name"].str.contains("FBtr0331261")
    Sxl_f.append(df[roi]["FPKM"].values)
    
    
    
Sxl_m= []
for sample in metadata[metadata["sex"] == "male"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/"+sample+"/t_data.ctab")
    roi = df ["t_name"].str.contains("FBtr0331261")
    Sxl_m.append(df[roi]["FPKM"].values)
    
Sxl_rf= []
for sample in replicates[replicates["sex"] == "female"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/"+sample+"/t_data.ctab")
    roi = df ["t_name"].str.contains("FBtr0331261")
    Sxl_rf.append(df[roi]["FPKM"].values)
    
Sxl_rm= []
for sample in replicates[replicates["sex"] == "male"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/"+sample+"/t_data.ctab")
    roi = df ["t_name"].str.contains("FBtr0331261")
    Sxl_rm.append(df[roi]["FPKM"].values)
        


    
plt.figure()
plt.plot(Sxl_f, 'r', label="female")
plt.plot(Sxl_m, 'b', label="male")
plt.plot(["4","5","6","7"], Sxl_rf, 'mo', label="replicate female")
plt.plot(["4","5","6","7"], Sxl_rm, 'go', label="replicate male")

plt.legend(loc='upper right', bbox_to_anchor=(0.5, 1.0))
plt.ylabel("mRNA abundance (FPKM)")
plt.xlabel("developmental stage")
plt.title("Sxl")
plt.xticks(range(len(Sxl_m)),["10","11", "12", "13", "14A", "14B", "14C", "14D"], rotation=90)
plt.savefig("timecourse.png")