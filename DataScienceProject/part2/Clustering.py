
# Unsupervised Learning - No outcome/not labeled.
import pandas
dataframe = pandas.read_csv("https://modcom.co.ke/data/datasets/AirlinesCluster.csv")
print(dataframe)

array = dataframe.values
X = array[:, 0:7]  # always a minus 1, its 6
# No Y
from sklearn.cluster import KMeans
model = KMeans(random_state=42, n_clusters=10)
model.fit(X)
print('Model Clustering ....Done!')

