import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
# create dataframe from csvfile.

df = pd.read_csv("../csv/clustering/year_clustering.csv")
cust_df = pd.read_csv("../csv/clustering/year_clustering.csv")

label = df["Year"].tolist()

print(label)

del(cust_df['Year'])
Z = linkage(cust_df, method="ward", metric="euclidean")

fig = plt.figure()



dendrogram(Z,
labels=label,
color_threshold=4)

dirname = "../output/"

plt.savefig(dirname + "image.png")

plt.show()
