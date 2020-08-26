
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
# step 2: Bring the training models
from sklearn.cluster import KMeans
model = KMeans(random_state=42, n_clusters=8)
model.fit(X)
print('Model clustering....Done!')

# Step 3: view your clusters
centronoids = model.cluster_centers_

clusters = pandas.DataFrame(centronoids,
                            columns=['FlightMiles','FlightTrans','DaysSinceEnroll'])

print(clusters)

# Step 4: get who is in these clusters, put them in excel worksheet, share them with ...
subset['label']  = model.labels_
subset = subset[subset['label'] == 3]

import xlwt
subset.to_excel("cluster3.xls", columns=['FlightMiles','FlightTrans','DaysSinceEnroll'])




