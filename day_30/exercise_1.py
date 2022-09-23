fruits = ["Apple", "Pear", "Orange"]



def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as e:
        print(f"fruits has only {len(fruits)} elements, starting from zero. You can't take value from index {index}")
    else:
        print(fruit + " pie")


make_pie(4)
