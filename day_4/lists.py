from pickle import TRUE


item1 = "item1"
item2 = 24
item3 = True
item4 = 2.5

lista = [item1,item2,item3,item4]
print(lista)
# print(lista[0])
# print(lista[-0])
# print(lista[-1])

lista[2] = False
print(lista)

lista.append("Appended string")
print(lista)

lista2 = [1,2]


#lista.append(lista2)

lista.extend(lista2)

print(lista)