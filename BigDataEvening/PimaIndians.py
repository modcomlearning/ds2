# Flower Classifier - Machine
import pandas
import sklearn
dataframe = pandas.read_csv('https://modcom.co.ke/data/datasets/pima.csv')
print(dataframe)

# Step 1: Split your datframe to features and outcome/label/target/output
array = dataframe.values

X = array[:, 0:8]   # upto the 3rd colm, always a -1  -Features
Y = array[:, 8]     # outcome/output


# balancing of classes
import imblearn
from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=42)
X_new, Y_new = smote.fit_sample(X,Y)  #


# Step 2: Split your X, Y into training set and testing set
from sklearn import model_selection
# 70% of 150 rows - training  set
# 30% of 150 rows - testing set
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X_new,Y_new,
                                                                    test_size=0.30,
                                                                    random_state=42) #42


# Step 3: Create algorithms for machine learning
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

# pick a model above fit X_train, Y_train
model = RandomForestClassifier(n_estimators=40)
model.fit(X_train,Y_train)  # we expose the X_train, Y_train to model
# Model learns from data in above code.
print('Learning..Training...')


# Step 4: We now ask the model, after learning - to predict x_test
predictions = model.predict(X_test)
print(predictions)

from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test, predictions)) # we check if predictions match the y-test

from sklearn.metrics import classification_report
print(classification_report(Y_test, predictions))

from sklearn.metrics import confusion_matrix
print(confusion_matrix(Y_test, predictions))

# Step 5: Use it, Deploy it, Optimize it.
predicted = model.predict([[2,2,45,180,22,11,22,180]])
print(predicted)