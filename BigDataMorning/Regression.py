
# regression when you predict a continous var, height, profit,
import pandas
dataframe = pandas.read_csv("https://modcom.co.ke/bigdata/datasets/Advertising.csv")
print(dataframe)

# Step 1: split your data to X, Y
array = dataframe.values   # get all values in your dataframe
X = array[:, 1:4]   # means 0 - 7 : Features
Y = array[:, 4]    # label/outcome/continous/

# Step 2: split your data to train/test
from sklearn import model_selection
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X,Y,
                                                                test_size=0.30,
                                                                random_state=7)

# Step 3: bring the models
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
