from asyncio.windows_events import NULL


def is_prime(number):
    if number == 0 or number == 1:
        print("0 and 1 are not in the discussion")
    else:
        for i in range(2,int(number/2)+1):
            if number % i == 0:
                print(f"{number} jest liczbą złożoną")
                return(False)
                break
            else:
                print(f"{number} jest liczbą pierwszą")
                return(True)
                break
         
n = int(input("Podaj liczbę, zobaczymy czy pierwsza  "))
is_prime(n)

