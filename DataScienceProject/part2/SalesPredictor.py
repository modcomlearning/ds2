
# Regression.
import pandas
dataframe = pandas.read_csv("https://modcom.co.ke/data/datasets/Advertising.csv")
print(dataframe)

# Step 1: split to X,Y
array = dataframe.values
# print(array)
X = array[:, 1:4] # always a -1 , upto 3: features
Y = array[:, 4]  # 8th counted here: outcome

# step 2: get your training set and test set
from sklearn import model_selection
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X,Y,
                                                                test_size=0.30,
                                                                random_state=42)