# FileNotFoundError
# KeyError
# IndexError
# TypeError

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["sdhds"])
# except KeyError as error_message:
#     print(f"The key {error_message} was not found")
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]


# def count_likes(posts):

#     total_likes = 0
#     for post in posts:
#         try:
#             total_likes = total_likes + post['Likes']
    
#         except KeyError:
#             continue
    
#     return total_likes


# print(count_likes(facebook_posts))

fruits = ["apple","banana","mango"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except:
        print("Fruit pie")
    else:
        print(fruit+"pie")

make_pie(4)