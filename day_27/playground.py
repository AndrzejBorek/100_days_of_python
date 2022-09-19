# def add(n1, n2):
#     return n1+n2
#
# print(add(1,2))
# def add(*args: int):
#     print(type(args))
#     print(args[0])
#     print(args[1])  # Can generate errors
#     sum = 0
#     for arg in args:
#         sum += arg
#     return sum
#
#
# print(add(1, 1, 1, 1, 1))


# def calculate(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#     print("kwargs ['add']:" + " " + str(
#         kwargs['add']))  # Can generate KeyError if add will not be in arguments when function is called
#

def calculate(n, **kwargs):
    try:
        n += kwargs['add']
    except KeyError:
        pass
    try:
        n *= kwargs['multiply']
    except KeyError:
        pass
    return n


print(calculate(1, multiply=4, add=3))


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get('model')


car = Car(make="Fiat", model="Punto")
print(car.model)
