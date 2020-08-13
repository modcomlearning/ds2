
# time series - working date/time
# How were sales overtime?
# How the profits overtime?
# How was the enrollment overtime?

import matplotlib.pyplot as plt
import pandas

# opsd_daily is the df  - dataframe
opsd_daily  = pandas.read_csv('https://modcom.co.ke/data/datasets/power.csv')
print(opsd_daily)

# check for empties
print(opsd_daily.isnull().sum())

# 2020/2/2, 1th August 2020, 1/2/2020, 2020-02-25,10-May-2020, August, 30, 2020

list = ['2020/2/2', '1st August 2020', '1/2/2020', '2020-02-25','10-May-2020',
        'August, 30, 2020', 'Oct 20, 1995','2/2021']

# pandas supports this date format : yyyy-mm-dd   2020-12-02
print(pandas.to_datetime(list))

