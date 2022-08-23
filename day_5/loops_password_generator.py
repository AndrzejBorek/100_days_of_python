import random as r
liczbaLiter = int(input("Ile liter ma mieć Twoje hasło? "))
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
hasło = ""
for i in range(0,liczbaLiter):
    los = r.randint(0,1)
    if los == 1:
        hasło = hasło + str(r.randint(0,9))
    else:
        hasło = hasło + r.choice(letters)

print(f"Twoje hasło to {hasło}")

