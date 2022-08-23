from math import ceil
from numpy import number


def paint_needed (height,width,coverage):
    number_of_cans = (height*width)/coverage
    return(ceil(number_of_cans))

height = float(input("How high is your wall? "))
width = float(input("How width is your wall? "))
coverage = float(input("How many square meters can one can cover? "))

number_of_cans = paint_needed(height=height,width=width,coverage=coverage)
print(f"Potrzebujesz {number_of_cans} puszek ")
