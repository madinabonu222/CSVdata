# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# data_dic = data.to_dict()
# print(data_dic)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
# print(sum(temp_list))
# temp_avg = sum(temp_list)/len(temp_list)
# print(temp_avg)
# # average = mean (median)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == (data.temp.max())])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp)
# celsius = monday.temp
# fahrenheit = (monday.temp * 1.8) + 32
# print(fahrenheit)

# Create a dataframe from scratch
# data_dic = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dic)
# data.to_csv("new_data.csv")

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dic = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
data = pandas.DataFrame(data_dic)
data.to_csv("squirrel_count.csv")

