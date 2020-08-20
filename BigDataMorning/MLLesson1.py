# supervised learning - in iris class is the outcome.
# classification

import pandas
pandas.set_option('display.max_rows', 150)
dataframe = pandas.read_csv("https://modcom.co.ke/bigdata/datasets/iris.csv")
print(dataframe)

import sklearn

# Step 1: split your data into features and outcome/target/label/output
array = dataframe.values   # get all values in your dataframe
X = array[:, 0:4]   # means 0 - 3 : Features
Y = array[:, 4]    # label/outcome

# Step 2: split data into training set and testing set
# use 70% of data for training
# use 30% of data for testing
from sklearn import model_selection
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X,Y,
                                                                test_size=0.30,
                                                                random_state=7)

# X_train is 70% of X, X_test is 30% of the X
# Y_train is 70% of Y, Y_test is 30% of the Y

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Step 3: Pick a model/algorithm
model = KNeighborsClassifier()
model.fit(X_train,Y_train) # we fit only the training set
print('Training....')
# Done
# Test your model with the 30% test set










