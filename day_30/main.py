# TypeError
# text = 'abc'
# try:
#     print(text + 5)
# except TypeError as e:
#     print("String + int can not be added")
#     print(e)
# else:
#     print("This line will execute if print(text+5) is valid code - so in this case, never")
# finally:
#     print("Finally this will be printed")
#

# # FIle not found
# try:
#     with open('should_throw_FileNotFoundError.txt', 'r') as f:
#         f.read()
# except FileNotFoundError as e:
#     print("This file does not exist so python can not open it")
#     print(e)

# Key error
# data = {"key": "value"}
#
# try:
#     value = data['not-key']
# except KeyError as e:
#     print(f"Data does not have key {e}")

# Index error
# fruits = ['Apple', 'Banana']
#
# try:
#     print(fruits[4])
# except IndexError as e:
#     print("fruits has only 2 indexes")
#     print(e)

height = float(input("Height: "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError("Human height should not be over 3 metres")

bmi = weight / height ** 2
print(bmi)
