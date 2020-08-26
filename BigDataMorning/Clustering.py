
# Supervised Learning. and Unsupervised Learning
# Unsupervised Learning - No outcome/target
import pandas

dataframe = pandas.read_csv("https://modcom.co.ke/bigdata/datasets/AirlinesCluster.csv")
print(dataframe)

# Step 1:
subset = dataframe[['FlightMiles','FlightTrans','DaysSinceEnroll']]
print(subset)

array = subset.values
X = array[:, 0:3]  # Means upto 2
# No outcome Y

from sklearn.cluster import KMeans
model = KMeans(n_clusters=5)
model.fit(X)  # we fit the X
print('Model creating clusters....Done!')

# get the center means
centronoids = model.cluster_centers_

clusters = pandas.DataFrame(centronoids,
                            columns=['FlightMiles','FlightTrans','DaysSinceEnroll'])

print(clusters)
