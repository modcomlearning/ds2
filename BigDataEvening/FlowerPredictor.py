# Flower Classifier - Machine
import pandas
import sklearn
dataframe = pandas.read_csv('https://modcom.co.ke/bigdataevening/datasets/iris.csv')
print(dataframe)

# Step 1: Split your datframe to features and outcome/label/target/output
array = dataframe.values

X = array[:, 0:4]   # upto the 3rd colm, always a -1  -Features
Y = array[:, 4]     # outcome/output

# Step 2: Split your X, Y into training set and testing set
from sklearn import model_selection
# 70% of 150 rows - training  set
# 30% of 150 rows - testing set
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X,Y,
                                                                    test_size=0.30,
                                                                    random_state=7)


# Step 3: Create algorithms for machine learning
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC