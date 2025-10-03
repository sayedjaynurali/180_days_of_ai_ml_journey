# with open("./weather_data.csv","r") as weather_data:
#     data = weather_data.readlines()

# print(data)

# import csv

# with open("./weather_data.csv","r") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

# data = pandas.read_csv("./weather_data.csv")

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]

# print(((monday.temp[0])*(9/5))+32)

# student_list = {
#     "student name": ["jay","pratik"],
#     "marks": [98, 95]
# }

# data = pandas.DataFrame(student_list)
# data.to_csv("./test_data.csv")

# data = pandas.read_csv("./Squirrel_Data.csv")

# colors = data["Primary Fur Color"]

# color_dict = {
#     "fur_color":["cinnamon","gray","black"],
#     "count":[0,0,0]
# }
# for color in colors:
#     if color == "Cinnamon":
#         color_dict["count"][0] += 1
#     elif color == "Gray":
#         color_dict["count"][1] += 1
#     elif color == "Black":
#         color_dict["count"][2] += 1

# count_data = pandas.DataFrame(color_dict)
# count_data.to_csv("./count_data.csv")

data = pandas.read_csv("./Squirrel_Data.csv")

cinnamon_squirel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_squirel_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirel_count = len(data[data["Primary Fur Color"] == "Black"])

color_dict = {
    "fur_color":["cinnamon","gray","black"],
    "count":[cinnamon_squirel_count,gray_squirel_count,black_squirel_count]
}

count_data = pandas.DataFrame(color_dict)
count_data.to_csv("./count_data.csv")