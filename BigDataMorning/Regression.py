
# regression when you predict a continous var, height, profit,
import pandas
dataframe = pandas.read_csv("https://modcom.co.ke/bigdata/datasets/Advertising.csv")
print(dataframe)

# Step 1: split your data to X, Y
array = dataframe.values   # get all values in your dataframe
X = array[:, 1:4]   # means 1-3 : Features
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor

model = LinearRegression()
model.fit(X_train, Y_train)
print('Training....')

# STep 4: testing

predictions = model.predict(X_test)
print(predictions)

# compare predictions with y_test, R squared gives the % performance
from sklearn.metrics import r2_score,mean_squared_error
print('Accuracy ', r2_score(Y_test, predictions))
print('Mean squared error', mean_squared_error(Y_test, predictions))
# MSE = 2.7 --Sqrt =  1.5
     # TV, Radio, newspaper
expense =  [[200,150,0]]
predicted = model.predict(expense)
print('You will sell ', predicted)


