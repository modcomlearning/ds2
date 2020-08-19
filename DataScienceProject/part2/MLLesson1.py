
import pandas
import matplotlib.pyplot as plt
dataframe = pandas.read_csv('https://modcom.co.ke/data/datasets/iris.csv')
print(dataframe)
# ML
# From iris , sepallength  sepalwidth  petallength  petalwidth - features
# From iris , class - outcome
# Supervised, we consider classification - outcome is categorical
# Step 1: split data to inputs(X) and outputs(y)
array = dataframe.values
X = array[:, 0:4] # 0 -3 colmns, always a -1  - features
Y = array[:, 4]   # 4th colmns - outcome/target

import sklearn

# Step 2 : split to training sets and testing sets
validation_size = 0.30  # 30% for testing/70% training
seed = 7  # for randomization

from sklearn import model_selection
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X,Y,
                                                            test_size=validation_size,
                                                                    random_state=seed)
# X, Y will be splitted into X_train, X_test, Y_train, Y_test
# X_train holds the 70% of the features
# X_test holds the 30% of the features

# Y_train holds the 70% of the output
# Y_test holds the 30% of the output
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

model = KNeighborsClassifier()
model.fit(X_train, Y_train) # done, learning from 70%







