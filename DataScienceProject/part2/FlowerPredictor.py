
import pandas
import matplotlib.pyplot as plt
import sklearn

dataframe = pandas.read_csv('https://modcom.co.ke/data/datasets/iris.csv')
print(dataframe)

# Step 1: split data into features and outcome
array = dataframe.values
# print(array)
X = array[:, 0:4] # always a -1 , upto 3: features
Y = array[:, 4]  # 4th counted here: outcome

# Step 2: split data into training set and test set.
# 70% for training , 30% for test set







