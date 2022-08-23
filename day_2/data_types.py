print(123_456_789 + 1) #_ treats like 123,456,789 dividing big numbers

#zadanie

x = input("Write integer")
x = str(x)
y = 0
for i in range(0,len(x)):
    y = y + int(x[i])

print(y)
