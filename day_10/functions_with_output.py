def test_2_return_values(a,b):
    return(a*b,a+b)

x,y = test_2_return_values(1,2)
print(x)
print(y)

x = test_2_return_values(1,2)
print(x)
print(type(x))

x,y = test_2_return_values(int(input("Podaj 1 liczbe")),int(input("Podaj 2 liczbe")))
print(x)
print(y)