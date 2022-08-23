
def divide(a,b):
    return (a/b)

def plus(a,b):
    return(a+b)

def minus(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def calculator():
    stay_in_calculator = True
    while stay_in_calculator:
        a = float(input("Give first number "))
        stay_with_value = True
        while stay_with_value == True:
            print("Available actions: ") 
            print(" + \n - \n *\n / \n")
            action = input("Choose action ")
            b = float(input("Choose second number: "))
            if action=="+":
                a = plus(a,b)
            elif action == "-":
                a = minus(a,b)
            elif action == "*":
                a = multiply(a,b)
            elif action == "/":
                a = divide(a,b)
            else:
                print("Wrong action")
                break
            print(f"Result is {a} ")
            choose = input("Type Y if you want to use the result further and N \n if you want to start new calculation or A if you want to exit calculator  ")
            if choose == "N":
                stay_with_value = False
            if choose == "A":
                stay_with_value = False
                stay_in_calculator = False


calculator()