

import matplotlib.pyplot as plt
import pandas
pandas.set_option('display.max_columns', 6)
pandas.set_option('display.max_rows', 50)
store  = pandas.read_csv('https://modcom.co.ke/data/datasets/superstore.csv',
                         parse_dates=['Order Date'], index_col=2)
#print(store)
print(store.dtypes)
print(store.isnull().sum())

# Describe data - works floats and ints
print(store.describe())
x, ax = plt.subplots()
store.groupby('Segment').size().plot(kind='pie', autopct = '%1.1f%%')
ax.set_title('Segment Distribution in %')
plt.savefig('plot15.png')

# stacked/unstacked bar
import numpy
# We have the Sales colm with a string
store['Sales'] = pandas.to_numeric(store['Sales'], errors='coerce')
store['Sales'].fillna(store['Sales'].median(), inplace=True)
print(store.dtypes)

x, ax = plt.subplots()
store.groupby(['Region','Segment'])['Sales'].mean().unstack().plot(kind='bar',
                                                                    stacked= False)
#ax.set_title('Average Reading marks by Gender and Rank')
plt.title('Average Reading marks by Gender and Rank')
plt.xlabel('Region')
plt.ylabel('Profit')
#ax.legend(loc='upper_center')
plt.legend(loc='best')
plt.savefig('plot16.png')


# time series
ax  = store.loc['2017-02', ['Profit']].plot()
ax.set_title('Profit  - Order Date')
ax.set_ylabel('Profit')
plt.savefig('plot17.png')
# End.
# Dashboard.













