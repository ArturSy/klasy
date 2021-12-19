#%%
import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename = 'month.csv'

with open(filename) as file:
    reader = csv.reader(file)
    header1 = next(reader)

#for index, column_header1 in enumerate(header1):
 #   print(index, column_header1)

    highs = []
    dates = []
    lows = []

    for row in reader:
        high = int(row[5])
        date = datetime.strptime(row[2], '%Y-%m-%d')
        low = int(row[6])
        highs.append(high)
        dates.append(date)
        lows.append(low)

print(highs)
print(dates)

fig, ax = plt.subplots()
ax.plot(dates, highs, c= 'red', label="highs")
ax.plot(dates, lows, c = 'blue', label= "lows")
ax.set_title('Najwyższe temperatury w lipcu')
ax.set_ylabel('Temperatura [F]')
fig.autofmt_xdate()
ax.legend()


plt.show()

# %%
