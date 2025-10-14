import random
import pandas
# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(num) for num in list_of_strings]
# result = [num for num in numbers if num%2 == 0]
# print(result)

# new_list = [(num*2) for num in range(1,5)]
# print(new_list)

# names = ["Jay","Priyasha","pratik","Rohan","mohandaskaramchandra"]
# new_list = [name.upper() for name in names if len(name)>5]
# print(new_list)

# import pandas
# file1 = pandas.read_csv("file1.txt")
# print(file1.to_dict())

# with open("./file1.txt") as file1:
#     list1 = [int(num.strip()) for num in file1]

# with open("./file2.txt") as file2:
#     list2 = [int(num.strip()) for num in file2]

# result = [num for num in list1 if num in list2]

# print(result)

# students = ["Jay","Pratik","Harsha"]
# mark_dict = {student:random.randint(1,100) for student in students}
# print(mark_dict)

# pass_dict = {key:value for (key,value) in mark_dict.items() if value >= 60}
# print(pass_dict)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words = sentence.split()
# result = {word:len(word) for word in words}
# print(result)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# weather_f = {key:((value * 9/5) + 32) for (key,value) in weather_c.items()}

# print(weather_f)

student_dict = {
    "student": ["Angela","James","Lilly"],
    "score": [29,32,95]
}

# for key,value in student_dict.items():
#     print(key)
#     print(value)

student_df = pandas.DataFrame(student_dict)

# for (key,value) in student_df.items():
#     print(key)
#     print(value)

for (index,row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)