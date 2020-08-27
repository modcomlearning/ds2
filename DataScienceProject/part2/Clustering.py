
# Unsupervised Learning - No outcome/not labeled.
import pandas
dataframe = pandas.read_csv("https://modcom.co.ke/data/datasets/AirlinesCluster.csv")
print(dataframe)

array = dataframe.values
X = array[:, 4:7]  # always a minus 1, its 6
# No Y

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 50):
     kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
     kmeans.fit(X)
     wcss.append(kmeans.inertia_)
plt.plot(range(1, 50), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.savefig("fig2.png")


from sklearn.cluster import KMeans
model = KMeans(random_state=42, n_clusters=14)
model.fit(X)
print('Model Clustering ....Done!')

# view the clusters
centronoids = model.cluster_centers_
clusters= pandas.DataFrame(centronoids,
                           columns=['FlightMiles','FlightTrans','DaysSinceEnroll'])

print(clusters)


# How to get the records in this cluster
dataframe['label']  = model.labels_
dataframe  = dataframe[dataframe['label'] == 0]

# above dataframe is filtered to cluster 5
import xlwt
dataframe.to_excel('cluster0.xls',
                   columns=['FlightMiles','FlightTrans','DaysSinceEnroll'])

