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

#ZADANIE : ile dni/tygodni/miesięcy zostało do 90 roku życia

wiek = int(input("Podaj swój wiek"))

lata = 90 - wiek
tygodnie = round(lata*52)
dni = round(tygodnie*7)

print(f"zostało Ci {lata} lat życia, co jest równe {tygodnie} tygodni i {dni} dni")