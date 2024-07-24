import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import NMF
from scipy.cluster.hierarchy import dendrogram, linkage


df = pd.read_excel('./normalized123.xlsx')
# Heat map
sns.heatmap(df)
plt.title('Heatmap of Data')
plt.show()


# CLUSTERING
# sns.clustermap(df, method='average', cmap='YlGnBu')
# sns.clustermap(df)
# plt.show()

# # Perform clustering
# clustergrid = sns.clustermap(df)

# # Get the row and column dendrogram linkage matrix
# row_linkage, col_linkage = clustergrid.dendrogram_row.linkage, clustergrid.dendrogram_col.linkage
# print(row_linkage, col_linkage)
# # You can use these linkages to further analyze or extract clusters
# # For example, using scipy's fcluster function to extract cluster labels
# from scipy.cluster.hierarchy import fcluster

# # Define a threshold or use the 'maxclust' method to specify the number of clusters
# threshold = 5
# clusters = fcluster(row_linkage, threshold, criterion='distance')
# print(clusters)
# # Now 'clusters' contains the cluster labels for each row in your DataFrame


# # Perform hierarchical clustering
# row_linkage = linkage(df, method='ward', metric='euclidean')

# # Plotting the dendrogram for row clusters
# plt.figure(figsize=(10, 7))
# dendrogram(row_linkage)
# plt.title("Dendrogram for Row Clustering")
# plt.xlabel("Index")
# plt.ylabel("Distance")
# plt.show()

# col_linkage = linkage(df.T, method='ward', metric='euclidean')  # Transpose the DataFrame to cluster columns

# print(col_linkage)

# # Plotting the dendrogram for column clusters

# plt.figure(figsize=(10, 7))

# dendrogram(col_linkage)

# plt.title("Dendrogram for Column Clustering")

# plt.xlabel("Index")

# plt.ylabel("Distance")

# plt.show()




# # NMF Section
# # Initialize NMF with n_components
# nmf = NMF(n_components=5, init='random', random_state=42)

# # Apply NMF
# W = nmf.fit_transform(df)
# H = nmf.components_

# print("M: ", W)

# print("  "," ")

# print("H: ", H)
