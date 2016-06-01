
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:\Users\marvin.marino\PycharmProjects\em-analytics\outflow.csv', header=0, sep=";", parse_dates=2)


## DATA PREPARATION ##


data['USCITA'] = data['USCITA'].str.replace(",", ".")  # replace "," with "."
data['USCITA'] = data['USCITA'].str.replace(ur"\u20ac", "") # \u20ac is encoding for euro symbol - not working!
data['USCITA'] = data['USCITA'].astype(float)

print data.head()



