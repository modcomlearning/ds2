

import pandas
dataframe = pandas.read_csv("https://modcom.co.ke/data/datasets/pima.csv")
print(dataframe)


# step 1:
import sklearn
# Step 1: split your data into features and outcome/target/label/output
array = dataframe.values   # get all values in your dataframe
X = array[:, 0:8]   # means 0 - 7 : Features
Y = array[:, 8]    # label/outcome


# there is a class imbalance
import imblearn
from imblearn.over_sampling import SMOTE
# virtual records.
smote = SMOTE(ratio= 'auto', kind = 'regular', random_state=42)

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
model = LinearDiscriminantAnalysis()
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


