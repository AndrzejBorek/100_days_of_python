


results = {
    "Andrzej":31,
    "Elli":79,
    "Ktoś tam:": 99
}

grades = {}
for value in results:
    if results[value]<=100 and results[value]>=80:
        grades[value]="Doskonale"
    elif results[value]>=50:
        grades[value]="OK"
    elif results[value]>=0 and results[value]<50:
        grades[value]="Słabo"
    else:
        print("Błędna wartość punktów")

print(grades)