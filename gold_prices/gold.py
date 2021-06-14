import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

df = pd.read_csv('./data/monthly_csv.csv')
# df = pd.read_csv('./data/annual_csv.csv')

dates_raw = df['Date']
timestamps = []
prices = df['Price']

for date in dates_raw:
    obj = datetime.datetime.strptime(date, '%Y-%m')
    timestamps.append(obj.timestamp())

fit = np.poly1d(np.polyfit(timestamps, prices, 2))
curve = np.linspace(min(timestamps), max(timestamps), 200)

plt.plot(timestamps, prices, '', curve, fit(curve))
plt.show()