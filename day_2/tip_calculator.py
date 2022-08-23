print("Welcome to the tip calculator")

bill = float(input("How much to pay?"))

tip = int(input("How big tip you wish to give?"))

persons = int(input("How many people to divide bill?"))

print(f"Every person should spend {round((bill+(tip/100)*bill)/persons,2)}")
