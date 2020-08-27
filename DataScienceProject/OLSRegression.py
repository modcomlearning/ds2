
# Regression.
import pandas
dataframe = pandas.read_csv("https://modcom.co.ke/data/datasets/Advertising.csv")
print(dataframe)

# Step 1: split to X,Y
array = dataframe.values
# print(array)
X = array[:, 1:2] # always a -1 , upto 3: features
Y = array[:, 4]  # 8th counted here: outcome



import statsmodels.api as sm
# Note the difference in argument order
model = sm.OLS(Y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print(model.summary())

print(model.predict([[50,40,20]]))



