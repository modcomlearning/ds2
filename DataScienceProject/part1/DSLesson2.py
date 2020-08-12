
import pandas
import matplotlib
# get this code here
# https://github.com/modcomlearning/ds2/blob/master/DataScienceProject/part1/DSLesson2.py

df = pandas.read_csv("https://modcom.co.ke/data/datasets/school.csv")
# df includes rows and colmns
print(df)
# are there empties?
print(df.isnull().sum())    # sum up empties/missing per colm
# do we work with empties/missing?
# imputation  - is fixing empty/missing records
# lets work with Rank, Gender, Reading, Math, Writing, SleepTime
subset = df[['Rank','Gender','Reading','Math','Writing','SleepTime']]
# we now work with subset
# Lest fill rank
subset['Rank'].fillna(5, inplace=True) # fillna fills missing and updates
subset['Gender'].fillna(2, inplace=True)

# get the median for reading
medianR = subset['Reading'].median()
subset['Reading'].fillna(medianR, inplace=True)  # Note that reading is continous

medianM = subset['Math'].median()
subset['Math'].fillna(medianM, inplace=True)

medianW = subset['Writing'].median()
subset['Writing'].fillna(medianW, inplace=True)

medianS = subset['SleepTime'].median()
subset['SleepTime'].fillna(medianS, inplace=True)

# confirm that missing is now filled for Rank, Gender, Reading, Math
print(subset.isnull().sum())


# replace Gender from 0, 1, 2 to Male and Female
subset['Rank'].replace({1:'Freshman', 2:'Sophomore',3:'Junior',4:'Senior', 5:'Missing'}, inplace=True)
subset['Gender'].replace({0:'Male', 1:'Female',2:'Missing'}, inplace=True)

print(subset.describe()) # basic stats, only works with
print(subset.corr())



# grouping
print(subset.groupby(['Gender'])['Math'].mean())
# pick from here
print(subset.groupby(['Rank'])['Math'].mean())

print(subset.groupby(['Rank'])['Reading'].mean())

print(subset.groupby(['Rank'])['Writing'].mean())

print(subset.groupby(['Rank'])['SleepTime'].mean())

print(subset.groupby(['Rank','Gender'])['SleepTime'].mean())

print(subset.groupby(['Rank','Gender'])['Reading'].mean())

print(subset.groupby(['Rank','Gender'])['Writing'].mean())


# plots
# Scatter plot  - numeric variables
import matplotlib.pyplot as plt

# plt is an Object, subplots is its behavior
# it returns tuple
x, ax = plt.subplots()
ax.scatter(subset['Reading'], subset['Math'], s=30, color='red')
ax.set_title('Reading vs Writing')
ax.set_xlabel('Math Marks(100%)')
ax.set_ylabel('Writing Marks(100%)')
plt.show()
plt.savefig('plot1.png')

# scatter plot can help in correlation, linear - Relationhsip between variables

# histogram - get frequency of a numeric variables
x, ax = plt.subplots()
ax.hist(subset['Math'], color = 'green')
ax.set_title('Math Distribution')
ax.set_xlabel('Math Marks(100%)')
ax.set_ylabel('Frequency')
plt.savefig('plot2.png')
plt.show()




















































