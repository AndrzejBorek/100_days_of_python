import random as r
names = "Andrzej,Elli,Asia,Marek"
people = names.split(",")

# l = r.randint(0,len(people)-1)
# print(f"{people[l]} will pay the bill")

#OR

person_to_pay = r.choice(people)
print(person_to_pay)