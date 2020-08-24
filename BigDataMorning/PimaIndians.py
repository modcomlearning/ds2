

import pandas
dataframe = pandas.read_csv("https://modcom.co.ke/data/datasets/pima.csv")
print(dataframe)


# step 1:
import sklearn
# Step 1: split your data into features and outcome/target/label/output
array = dataframe.values   # get all values in your dataframe
X = array[:, 0:8]   # means 0 - 7 : Features
Y = array[:, 8]    # label/outcome


# feature selection
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=40)
rfe  = RFE(rfc, 5)
fitted = rfe.fit(X,Y)
print("Selected %s" % (fitted.support_))


# there is a class imbalance
import imblearn
from imblearn.over_sampling import SMOTE
# virtual records.
smote = SMOTE( random_state=42)

X_new , Y_new = smote.fit_sample(X,Y)
# X_new, Y_new now have equal Positive/Negative, it raised the positives with virtual data


from sklearn import model_selection
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X_new,Y_new,
                                                                test_size=0.30,
                                                                random_state=7)


from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Step 3: Pick a model/algorithm
model = RandomForestClassifier()
model.fit(X_train,Y_train) # we fit only the training set
print('Training....')


predictions = model.predict(X_test) # we hide Y_test , original outcomes
#print(predictions)
#print(Y_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test, predictions))

from sklearn.metrics import confusion_matrix
print(confusion_matrix(Y_test, predictions))

from sklearn.metrics import classification_report
print(classification_report(Y_test, predictions))

newpatient = [[3,170,80,60,100,28,0.800,75]]
predicted = model.predict(newpatient)
print(predicted)
# RFE   - pic the top features and eliminate features that were not performing
# Feature selection

