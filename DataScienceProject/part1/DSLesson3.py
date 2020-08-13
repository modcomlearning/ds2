
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

ax= opsd_daily.loc['2016',['Consumption']].plot()
ax.set_title('Power Consumption in 2016')
ax.set_ylabel('Power Consumption(Ghz)')
plt.savefig('plot10.png')


ax= opsd_daily.loc['2016',['Wind']].plot()
ax.set_title('Wind Production in 2016')
ax.set_ylabel('Wind (Ghz)')
plt.savefig('plot11.png')

ax= opsd_daily.loc['2016',['Solar']].plot()
ax.set_title('Solar Production in 2016')
ax.set_ylabel('Solar(Ghz)')
plt.savefig('plot12.png')









