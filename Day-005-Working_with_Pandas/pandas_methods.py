import pandas

# Reading the Data
data = pandas.read_csv("./weather_data.csv")

# Type conversion of Series and DF
# print(type(data))
# print(data["temp"].to_list())
# print(data.to_dict())

# Series Methods
# print(data["temp"].mean())
# print(data["temp"].max())

# Get Data in columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == data["temp"].max()])

# Get a Particular column in a row
# wednesday = data[data["day"] == "Wednesday"]
#Clarification
# print(wednesday["temp"][2]) #returns row with index label 2 only if the selected row has index label 2
# print(type(wednesday.temp[0])) #returns the first element of the selected row as no matter the label
# Task
# c_temp = wednesday["temp"].iloc[0] #does the same work as above does
# k_temp = c_temp+273
# print(k_temp)

# Creating a Dataframe from Scratch
# test_dict = {
#     "names": ["jay","kuldip","pratik"],
#     "scores": [100,99,98]
# }
# test_df = pandas.DataFrame(test_dict)
# test_df.to_csv("./test_data.csv")

