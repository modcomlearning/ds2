
# import pandas
import pandas
import matplotlib
# installing through terminal   - View - Tool Windows - Terminal
# use 'pip install pandas'
mydata = pandas.read_csv("https://modcom.co.ke/data/datasets/sales.csv")
#mydata = pandas.read_csv("sales.csv")
print(mydata) # the whole data set
print(mydata['category'])  # show individual colm
print(mydata.shape)   # how many rows/columns

# get the colms names
for column in mydata.columns:
    print(column)

# statistics
stats = mydata.describe()
print(stats)

# statistics, graphs,matplotlib,




















