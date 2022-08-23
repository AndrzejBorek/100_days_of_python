print("Welcome to the tip calculator")

rachunek = float(input("Ile wyszedł rachunek?"))

tip = int(input("Ile chciałbyś procent napiwku dać?"))

osoby = int(input("Na ile osób chciałbyś podzielić rachunek?"))

print(f"Każda osoba powinna wydać {round((rachunek+(tip/100)*rachunek)/osoby,2)}")