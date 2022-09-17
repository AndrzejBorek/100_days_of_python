# numbers = [n for n in range(1, 27)]
#
# squared_numbers = [n * n for n in numbers]
# print(squared_numbers)
#
# even_numbers = [n for n in numbers if n % 2 == 0]
# print(even_numbers)
#
# with open('file1.txt') as f1:
#     file_1_list = [int(n) for n in f1.readlines()]
#
# with open('file2.txt') as f2:
#     file_2_list = [int(n) for n in f2.readlines()]
#
# ending_list = [n for n in file_1_list if n in file_2_list]
# print(ending_list)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# dict_of_words_with_length = {word: len(word) for (word) in sentence.split()}
# print(dict_of_words_with_length)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {key: (value*9/5+32) for (key, value) in weather_c.items()}
print(weather_f)
