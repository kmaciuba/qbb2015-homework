#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/USERS/cmdb/qbb2015/rawdata/samples.csv"
annotation2="/USERS/cmdb/qbb2015/stringtie/"

df = pd.read_csv(annotation)


for i in df["sample"]:
    df2= pd.read_table("/USERS/cmdb/qbb2015/stringtie/"+i+"/t_data.ctab")
    roi=df2["t_name"].str.contains("FBtr0331261")
    print df2[roi]
 
 
