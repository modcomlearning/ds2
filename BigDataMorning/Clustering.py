
# Supervised Learning. and Unsupervised Learning
# Unsupervised Learning - No outcome/target
import pandas

dataframe = pandas.read_csv("https://modcom.co.ke/bigdata/datasets/AirlinesCluster.csv")
print(dataframe)

# Step 1:
subset = dataframe[['FlightMiles','FlightTrans','DaysSinceEnroll']]
print(subset)

