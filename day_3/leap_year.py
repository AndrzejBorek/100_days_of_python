
def is_leap(rok):
    if rok % 4 ==0:
        if rok % 100 == 0:
            if rok % 400 == 0:
                print(f"Rok {rok} jest przestępny ")
            else:
                print(f"Rok {rok} nie jest przestępny ")
        else:
            print(f"Rok {rok} jest przestępny ")
    else:
        print(f"Rok {rok} nie jest przestępny ")

rok = int(input("Podaj rok zobaczymy czy przestepny "))
is_leap(rok)
