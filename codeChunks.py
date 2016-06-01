

# use this to set decimal
data = pd.read_csv('C:\Users\marvin.marino\PycharmProjects\em-analytics\outflow.csv', header = 0, sep = ";", parse_dates = 2, decimal= ",")

# example apply function
def valuation_formula(x, y):
    return x * y * 0.5

df['price'] = df.apply(lambda row: valuation_formula(row['x'], row['y']), axis=1)


# setting date format
from datetime import datetime # for strptime function
data['DATA'] = data['DATA'].apply(lambda d: datetime.strptime(d, "%dd%mm%yyyy"))

# removing all non chars
data['USCITA'] = data['USCITA'].str.replace(r"[^0-9]", "")  # remove euro symbol by removing all non-char

# encoding
data = pd.read_csv('C:\Users\marvin.marino\PycharmProjects\em-analytics\outflow.csv', header=0, sep=";", parse_dates=2)

data = pd.read_csv('C:\Users\marvin.marino\PycharmProjects\em-analytics\outflow.csv', header=0, sep=";", parse_dates=2, encoding="cp1252")
data = pd.read_csv('C:\Users\marvin.marino\PycharmProjects\em-analytics\outflow.csv', header=0, sep=";", parse_dates=2, encoding="utf_8")

import sys
reload(sys)
sys.setdefaultencoding('UTF8')

utf_8

data['USCITA'] = data['USCITA'].apply(lambda x: x.replace(u"\u20AC", " "))  # strip eur sign / does not work on float?

# 2. Coerce date as date
# data['DATA'] = data['DATA'].date.astype("datetime64") # not working