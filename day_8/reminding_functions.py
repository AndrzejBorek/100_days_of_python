from numpy import greater_equal


def gretting():
    print(" 1st greet\n 2nd greet\n 3rd greet")
gretting()

def greeting_with_name(name):
    print(f"Hello {name} ")

greeting_with_name("Andrzej")
greeting_with_name(2)

# def greetings_with_two_names(name,name2):
#     print(f"Hello {name} and hello {name2} ")
# greetings_with_two_names("Andrzej","Eli")

#MOŻNA TEŻ:

def greetings_with_two_names(name,name2):
    print(f"Hello {name} and hello {name2} ")
greetings_with_two_names(name2 = "Eli",name ="Andrzej") 


