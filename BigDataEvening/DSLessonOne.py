# pandas helps in data preparation.
import pandas

# matplotlib - creating graphs, plots
import matplotlib
data = pandas.read_csv("https://modcom.co.ke/bigdataevening/datasets/iris.csv")
print(data)
# basic descriptive stats
print(data.describe()) # numeric

# force sepalwidth to numeric
data['sepalwidth'] = pandas.to_numeric(data['sepalwidth'], errors='coerce')
# above will make the ? , to be nan
data['sepalwidth'].fillna(data['sepalwidth'].median(), inplace=True) # update
data['petallength'].fillna(data['petallength'].median(), inplace=True) # update

# describe again
print(data.describe())
# correlation
# when one goes up, the other goes up -:  0  -  1  : Positive
# when one goes up, the other goes down -:  0 -  -1  : Negative
print(data.corr())

# plots from piecharts, bar, pie, histograms, stacked bars, density plots, heatmaps
import matplotlib.pyplot as plt
# univariate , bivariate, multivariate plots
# histogram, box, density - check some variable with a freq - univariate

x, y = plt.subplots()
y.hist(data['sepalwidth'], color = 'green')
y.hist(data['sepalwidth'], color = 'red')
plt.title('Sepal Width Distribution')
plt.xlabel('sepalwidth - cm')
plt.ylabel('Freq.')
plt.savefig('fig1.png')


x, y = plt.subplots()
y.scatter(data['petalwidth'], data['petallength'] , color = 'red')
plt.title('sepalwidth vs sepallength')
plt.xlabel('petalwidth -cm')
plt.ylabel('petallength -cm')
plt.savefig('fig2.png')


# density plots
x, y = plt.subplots()
y.plot(data['petalwidth'], color = 'orange', label= 'Petal Width - cms')
y.plot(data['petallength'], color = 'red', label= 'Petal Length - cms')
y.plot(data['sepalwidth'], color = 'green', label= 'Sepal Width -cms')
plt.title('petalwidth vs petallength vs sepalwidth')
plt.xlabel('Freq.')
plt.ylabel('')
y.legend(loc='best') # puts the legen on the best location
plt.savefig('fig3.png')










