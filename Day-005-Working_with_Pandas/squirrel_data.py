import pandas

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