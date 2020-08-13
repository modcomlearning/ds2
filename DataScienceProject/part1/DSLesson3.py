
# time series - working date/time
# How were sales overtime?
# How the profits overtime?
# How was the enrollment overtime?

import matplotlib.pyplot as plt
import pandas

# opsd_daily is the df  - dataframe
opsd_daily  = pandas.read_csv('https://modcom.co.ke/data/datasets/power.csv',
                              parse_dates=['Date'] , index_col=0)
print(opsd_daily)

# check for empties
print(opsd_daily.isnull().sum())
# plots
plt.style.use('seaborn')

ax= opsd_daily.loc['2017','Consumption'].plot()
ax.set_title('Power Consumption in 2018')
ax.set_ylabel('Power Consumption(Ghz)')
plt.savefig('plot10.png')










