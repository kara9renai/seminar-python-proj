# import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
# create dataframe from csvfile.

df = pd.read_csv("../csv/clustering/ctry_clustering.csv")
cust_df = pd.read_csv("../csv/clustering/ctry_clustering.csv")

label = df["Country"].tolist()

print(label)

del(cust_df['Country'])
Z = linkage(cust_df, method="ward", metric="euclidean")

fig = plt.figure()



dendrogram(Z,
labels=label,
color_threshold=4)

"""
画像を保存する
dirname = "../output/"

plt.savefig(dirname + "image.png")
"""

plt.show()