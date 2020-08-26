
# Supervised   Learning - Classification, Regression
# Unsupervised Learning - Clustering *
import pandas
dataframe =pandas.read_csv("https://modcom.co.ke/bigdataevening/datasets/AirlinesCluster.csv")
print(dataframe)

# We find  customers with similar x-tics, narrow to clusters
subset = dataframe[['FlightMiles','FlightTrans','DaysSinceEnroll']]
print(subset)