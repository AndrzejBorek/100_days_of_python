import random as r
x = int(input("Choose 0 for rock, 1 for paper, 2 for scissors "))

names = ["rock","paper","scissors"]

computer_choose = [0,1,2]

choose = r.randint(0,2)

choose = computer_choose[choose]

print(f"Computer chooses {names[choose]}")

if x==0:
    if choose == 1:
        print(f"{names[choose]} beats {names[x]}")
    elif choose == 2:
        print(print(f"{names[x]} beats {names[choose]}"))
    else:
        print("draw")
elif x==1:
    if choose == 2:
        print(f"{names[choose]} beats {names[x]}")
    elif choose == 0:
        print(print(f"{names[x]} beats {names[choose]}"))
    else:
        print("draw")
elif x==2: 
    if choose == 0:
        print(f"{names[choose]} beats {names[x]}")
    elif choose == 1:
        print(print(f"{names[x]} beats {names[choose]}"))
    else:
        print("draw")