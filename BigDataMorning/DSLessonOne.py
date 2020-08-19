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
# histogram - univariate
x, y  = plt.subplots()
y.hist(dataframe['sepallength'], color= 'blue')
plt.title('Distribution of sepallength')
plt.xlabel('sepallength - cm')
plt.ylabel('Freq')
plt.savefig('fig1.png')


# scatter plot  - shows relationship between 2 variables
x, y = plt.subplots()
y.scatter(dataframe['sepallength'], dataframe['petalwidth'] , color = 'green')
plt.title('Relation between sepallength & petal width')
plt.xlabel('sepallength -cm')
plt.ylabel('petalwidth -cm')
plt.savefig('fig2.png')

# histogram for - petalwidth, petallength
# scatter of - petalwidth, petallength
# 0729 225 710
# TeamViewer
print(dataframe.groupby('class').size())
print(dataframe.groupby('class').mean())
print(dataframe.groupby('class').describe())

# pie chart
x, y = plt.subplots()
dataframe.groupby('class').size().plot(kind='pie', autopct = '%2.2f%%',
                                       explode =(0,0.1,0.2))
plt.title('Proportion of flower class in %')
plt.xlabel('')
plt.ylabel('')
plt.savefig('fig3.png')

# bar chart
x, y = plt.subplots()
dataframe.groupby('class')['petalwidth'].mean().plot(kind='bar')
plt.xlabel('Flower Class')
plt.ylabel('Petal Width -cms')
plt.savefig('fig4.png')

# line plots, scatter, density
# density - univariate
x, y = plt.subplots()
y.plot(dataframe['petalwidth'], color= 'orange')
plt.xlabel('Freq.')
plt.ylabel('petalwidth')
plt.savefig('fig5.png')






























