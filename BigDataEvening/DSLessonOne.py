# pandas helps in data preparation.
import pandas

# matplotlib - creating graphs, plots
import matplotlib
data = pandas.read_csv("https://modcom.co.ke/bigdataevening/datasets/iris.csv")
print(data)
# basic descriptive stats
print(data.describe()) # numeric


# force sepalwidth to numeric
#
data['sepalwidth'] = pandas.to_numeric(data['sepalwidth'], errors='coerce')
# above will make the ? , to be nan
data['sepalwidth'].fillna(data['sepalwidth'].median(), inplace=True) # up[date