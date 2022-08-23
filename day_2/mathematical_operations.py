# 2+2
# 2-2
# 2*2
# 2/2 
# 2**3 #2 to power 3

#BMI:

# weight = float(input("enter weight in kg "))
# height = float(input ("enter height in m "))

# bmi = weight/(height**2)
# print(f'{bmi:.2f}')
# #or
# print(round(bmi,2))

#rounding:

# print(8 / 3)
# print(8 // 3)

# result = 4/2
# result /= 2 #shorter way to write result = result / 2
# print (result)

#Task : how much time until 90th year of life

age = int(input("Podaj swój wiek"))

years = 90 - age
weeks = round(years*52)
days = round(weeks*7)

print(f"you have left {years} lat życia, co jest równe {weeks} tygodni i {days} dni")
