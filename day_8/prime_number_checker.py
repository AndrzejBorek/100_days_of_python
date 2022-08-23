from asyncio.windows_events import NULL


def is_prime(number):
    if number == 0 or number == 1:
        print("0 and 1 are not in the discussion")
    else:
        for i in range(2,int(number/2)+1):
            if number % i == 0:
                print(f"{number} is not prime")
                return(False)
                break
            else:
                print(f"{number} is prime")
                return(True)
                break
         
n = int(input("Lets see if this number is prime  "))
is_prime(n)

