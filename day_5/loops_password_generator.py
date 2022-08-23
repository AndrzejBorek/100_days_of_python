import random as r
numberOfLetters = int(input("How many letters in password? "))
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = ""
for i in range(0,numberOfLetters):
    los = r.randint(0,1)
    if los == 1:
        password = password + str(r.randint(0,9))
    else:
        password = password + r.choice(letters)

print(f"Your password is {password}")

