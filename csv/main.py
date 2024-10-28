# with open("weather_data.csv") as f:
#     data = f.readlines()
#     print(data)

# import csv
#
# temperature = []
# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     headings = next(data)
#     for d in data:
#         temperature.append(int(d[1]))
#
#     print(temperature)

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# temp = data['temp']
# print(type(temp))
# print(temp.max())
# data[condition] to get row

#print(data[data.temp== data.temp.max()])

# monday = data[data.day=="Monday"]
# print( 2* monday.temp)

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240810.csv')
#print(data['Primary Fur Color'][:50])
counts = data['Primary Fur Color'].value_counts()
#print(type(counts))
counts.to_csv('small.csv')