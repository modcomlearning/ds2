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

