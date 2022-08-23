############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

#i actually never got to 20, as in method description it goes from i,i+1,i+2...j-1 in our case i = 1, j = 20

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"] # In python index of table start with 0
# dice_num = randint(1, 6) #this method can return number from 1 to 6 with step 1.
# print(dice_imgs[dice_num]) # So stattistically 1 in 6 attempts will throw IndexError because there is no dice_imgs[6]\
# #to reproduce bug we can simply: print(dice_imgs[6])
# #to fix it we need to assign: dice_num = randint(0,5)

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

#This code won't do anything if year is equal to 1980,1994, or less than 1980


# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# print instruction in line 33 has to be intended, also we can't compare int (18) with strings (input("How old are you"))

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) #in this line we are not assigning input to word_per_page but we check equality between them 
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)  #If we want to print table [2,4,6,10,16,26] we should intend this line, because now its only apending one value - last value from a_list multiplied by 2
#   print(b_list)

# mutate([1,2,3,5,8,13])