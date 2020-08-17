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










