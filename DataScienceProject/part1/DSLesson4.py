

import matplotlib.pyplot as plt
import pandas
pandas.set_option('display.max_columns', 6)
pandas.set_option('display.max_rows', 50)
store  = pandas.read_csv('https://modcom.co.ke/data/datasets/superstore.csv')
#print(store)
print(store.dtypes)
print(store.isnull().sum())

# Describe data - works floats and ints
print(store.describe())

x, ax = plt.subplots()
store.groupby('Segment').size().plot(kind='pie', autopct = '%1.1f%%')
ax.set_title('Segment Distribution in %')
plt.savefig('plot15.png')