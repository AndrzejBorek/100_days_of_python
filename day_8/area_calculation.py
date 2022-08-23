from math import ceil
from numpy import number


def paint_needed (height,width,coverage):
    number_of_cans = (height*width)/coverage
    return(ceil(number_of_cans))

height = float(input("Ile metrów wysokości ma twoja ściana? "))
width = float(input("Ile metrów szerokości ma twoja ściana? "))
coverage = float(input("Jakie pokrycie ma jedna puszka? "))

number_of_cans = paint_needed(height=height,width=width,coverage=coverage)
print(f"Potrzebujesz {number_of_cans} puszek ")
