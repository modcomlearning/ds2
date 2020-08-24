# regression
import pandas

dataframe = pandas.read_csv("https://modcom.co.ke/bigdataevening/datasets/Advertising.csv")
print(dataframe)

# we are predicting the sales - continous variable - regression
array = dataframe.values
X = array[:, 1:4]   # upto the 3rd colm, always a -1  -Features
Y = array[:, 4]     # outcome/output/sales

from sklearn import model_selection
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X,Y,
                                                                    test_size=0.30,
                                                                    random_state=42) #42

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, Y_train)
print('Model Learning Complete')

predictions = model.predict(X_test)
print(predictions)

from sklearn.metrics import r2_score
print('Accuracy ', r2_score(Y_test, predictions))

