

import pandas as pd
import matplotlib.pyplot as plt

import dateutil  # for data parser


data = pd.read_csv('C:\Users\marvin.marino\PycharmProjects\em-analytics\outflow.csv',
                   header=0,
                   sep=";",
                   parse_dates=2,
                   encoding="cp1252")

# DATA PREP

# clean-up
data['USCITA'] = data['USCITA'].str.replace(".", "")  # replace . with nothing
data['USCITA'] = data['USCITA'].str.replace(",", ".")  # replace , with .
data['USCITA'] = data['USCITA'].str.replace(u"\u20AC", "")  # strip eur sign

### FIX - coerce date as date
# data['DATA'] = pd.to_datetime(data['DATA'], unit='s')
# data['DATA'] = data['DATA'].apply(dateutil.parser.parse, dayfirst=True) # does not work

# coherce uscita as float?

# Rename columns?

# print summary
print data.head()
print data.dtypes

#### BEGIN TESTING #####

# SUMMARIZE DATASET
# check this article:
# http://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/

## TEST - some general summarisation
print data['USCITA'].count()  # how many rows
print data['USCITA'].max()  # highest expense
print data['USCITA'][data['ID_S'] == 'Manutenzione'].sum()  # total of maintenance

## TEST - aggregate USCITA by weeks, months
byDate = data['USCITA'].groupby(data['DATA'])
print byDate.groups.keys()

data.groupby('month')

#### END TESTING #####


# PLOTS

# plot uscita as time series
ts = data['USCITA']
plt.plot(ts)
plt.show()

