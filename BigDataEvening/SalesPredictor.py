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
                                                                    random_state=7) #42