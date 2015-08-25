#!/usr/bin/env python

import pandas as pd

annotation = "/USERS/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment='#', header= None)

#print df,
#print df.head()
#print df.describe()
#print df.info()

#print "\nThis is what happens when you use df[1:5]\n"
#print df[1:5] #end number not inclusive

#show rows 10 through 15 (1-based, inclusive)
#print df[9:15]
#show rows 20-25
#print df[19:25]

#print df.info()
df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attribute"]
#print df.info()


#(columns="type")
#print df.sort("type")
#print df["chromosome"]
#Subset chromosome, start, and end columns
#print df[[ "chromosome", "start", "end" ]] #[] makes it a list

#print df["start"][9:15]

#print df.shape
#df2= df["start"]
#print df2.shape

#df2.to_csv("startColumn.txt", sep='\t', index=False)

#print df.shape
roi = df["start"] < 10
#print roi.shape
#print df[roi]
print df[roi].shape





