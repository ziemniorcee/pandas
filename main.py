# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
# print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].tolist()
# print(temp_list)
# ave = data["temp"].mean()
# max1 = data["temp"].max()
#
# # Get row
# monday = data[data["day"] == "Monday"]
# print(int(monday["temp"]) * (9/5) +32)

# Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# datas = pandas.DataFrame(data_dict)
# print(datas)
# datas.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = ["Gray", "Black", "Cinnamon"]
count = []
for color in colors:
    count.append(len(data[data["Primary Fur Color"] == color]))

data_dict = {
    "Fur Color":  colors,
    "count": count,
}

final = pandas.DataFrame(data_dict)
final.to_csv("squirrel_count.csv")