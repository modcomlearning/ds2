# pandas helps in data preparation.
import pandas

# matplotlib - creating graphs, plots
import matplotlib
data = pandas.read_csv("https://modcom.co.ke/bigdataevening/datasets/iris.csv")
print(data)
# basic descriptive stats
print(data.describe()) # numeric
print(data.dtypes)

# force sepalwidth to numeric

data['sepalwidth'].replace({'?': 0} , inplace=True)
pandas.to_numeric(data['sepalwidth'])

