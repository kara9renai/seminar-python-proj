import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
# create dataframe from csvfile.

df = pd.read_csv("year_clustering.csv")
cust_df = pd.read_csv("year_clustering.csv")

label = df["Year"].tolist()

print(label)

del(cust_df['Year'])
Z = linkage(cust_df, method="ward", metric="euclidean")

fig = plt.figure()



dendrogram(Z,
labels=label,
color_threshold=4)

plt.show()