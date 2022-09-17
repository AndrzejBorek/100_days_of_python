numbers = [1, 2, 3]

# Classic way
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)

# List comprehension:
new_list_2 = [n + 1 for n in numbers]

print(new_list_2)

doubled_list = [n * 2 for n in range(1, 5)]
print(doubled_list)

names = ["Alex", 'Beth', 'Caroline', 'Dave', 'Very_long_name']

short_names = [name for name in names if len(name) < 5]
print(short_names)
