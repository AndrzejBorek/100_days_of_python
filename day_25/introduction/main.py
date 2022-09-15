# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv


# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data['temp'])
#
# print(type(data))
# print(type(data['temp']))  # Single column of data frame is series
#
# data_dict = data.to_dict()
# print(data_dict)
#
# data_temp_series = data['temp'].to_list()
# print(data_temp_series)
#
# print(data['temp'].mean())
#
# print(data['temp'].max())
#
# print(data['condition'])
#
# print(data.condition)

# Get data in row

# print(data[data.day == 'Monday'])
#
# print(data[data.temp == data.temp.max()])
#
# print(data[data.temp == data.temp.max()].day)

# Monday temp to fahrenheit

# monday_temp = int(data[data.day == 'Monday'].temp)
#
#
# def celcius_to_fahrenheit(temp: int):
#     return temp * (9 / 5) + 32
#
#
# print(celcius_to_fahrenheit(monday_temp))

# Create data frame from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data=data_dict)
#
# data.to_csv("new_data.csv")
# print(data)
