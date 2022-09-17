list_of_values = [1, 2, 3]

dict_of_values = {1: 1, 2: 2, 3: 3}

new_dict_from_list = {item: item + 1 for item in list_of_values}
print(new_dict_from_list)

new_dict_from_dict = {key + 1: value + 1 for (key, value) in dict_of_values.items()}
print(new_dict_from_dict)

new_dict_from_dict_with_check = {key + 1: value + 1 for (key, value) in dict_of_values.items() if key % 2 == 0}
print(new_dict_from_dict_with_check)
