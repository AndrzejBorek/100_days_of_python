
def is_leap(rok):
    if rok % 4 ==0:
        if rok % 100 == 0:
            if rok % 400 == 0:
                print(f"Year {rok} is leap ")
            else:
                print(f"Year {rok} is not leap ")
        else:
            print(f"Year {rok} is leap ")
    else:
        print(f"Year {rok} is not leap")

rok = int(input("Give year lets see if its leap "))
is_leap(rok)
