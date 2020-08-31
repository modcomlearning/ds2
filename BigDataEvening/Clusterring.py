
# Supervised   Learning - Classification, Regression
# Unsupervised Learning - Clustering *
import pandas
dataframe =pandas.read_csv("https://modcom.co.ke/bigdataevening/datasets/AirlinesCluster.csv")
print(dataframe)

# We find  customers with similar x-tics, narrow to clusters
subset = dataframe[['FlightMiles','FlightTrans','DaysSinceEnroll']]
print(subset)

# step 1: create your features
array = subset.values
X  = array[:, 0:3]  # theres a munus 1
# No Y/Outcome.
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
from sklearn.cluster import KMeans
wcss = []
for i in range(1,100):
     kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
     kmeans.fit(X)
     wcss.append(kmeans.inertia_)
plt.plot(range(1, 100), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.savefig("fig1.png")

# step 2: Bring the training models
from sklearn.cluster import KMeans
model = KMeans(random_state=42, n_clusters=15)
model.fit(X)
print('Model clustering....Done!')

# Step 3: view your clusters
centronoids = model.cluster_centers_

clusters = pandas.DataFrame(centronoids,
                            columns=['FlightMiles','FlightTrans','DaysSinceEnroll'])

print(clusters)

# Step 4: get who is in these clusters, put them in excel worksheet, share them with ...
subset['label']  = model.labels_
subset = subset[subset['label'] == 12]

import xlwt
subset.to_csv("cluster6.csv", columns=['FlightMiles','FlightTrans','DaysSinceEnroll'])

# 0729 225 710