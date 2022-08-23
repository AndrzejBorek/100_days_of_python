print(123_456_789 + 1) #_ traktuje jak 123,456,789 - rozdzielenie dużych liczb

#zadanie

x = input("Write integer")
x = str(x)
y = 0
for i in range(0,len(x)):
    y = y + int(x[i])

print(y)