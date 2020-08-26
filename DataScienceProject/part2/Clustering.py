
# Unsupervised Learning - No outcome/not labeled.
import pandas
dataframe = pandas.read_csv("https://modcom.co.ke/data/datasets/Customers.csv")
print(dataframe)

array = dataframe.values
X = array[:, 4:7]  # always a minus 1, its 6
# No Y
from sklearn.cluster import KMeans
model = KMeans(random_state=42, n_clusters=10)
model.fit(X)
print('Model Clustering ....Done!')

# view the clusters
centronoids = model.cluster_centers_
clusters= pandas.DataFrame(centronoids,
                           columns=['FlightMiles','FlightTrans','DaysSinceEnroll'])

print(clusters)
