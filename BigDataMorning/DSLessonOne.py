# pandas - for data prep, clean, munging

import pandas
# matplotlib  - for visualization
import matplotlib

# scikit learn  - Machine learning, Models, LR, KNN, RF,
import sklearn

# pandas.pydata.org
#print(dir(sklearn))
# dataframe has rows and colms
pandas.set_option('display.max_rows', 150)
dataframe = pandas.read_csv("https://modcom.co.ke/bigdata/datasets/iris.csv")
print(dataframe)
# Type of data: Numeric, Categorical/Norminal - categories, no order, Male/Female
# Ordinal - Categorical - there is an order : low, medium, high
# descriptive  - describing your data
print(dataframe.describe())

# correlation, how variables are correlated with each other
# ones up , other goes down - Negative -  0  to -1
# ones up, the other up   - Positive   - 0 to 1
print(dataframe.corr())

# plots
import matplotlib.pyplot  as plt
# histogram
x, y  = plt.subplots()
y.hist(dataframe['sepallength'], color= 'blue')
plt.title('Distribution of sepallength')
plt.xlabel('sepallength - cm')
plt.ylabel('Freq')
plt.savefig('fig1.png')













