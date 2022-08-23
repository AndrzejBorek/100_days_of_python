row1 = ["1","2","3"]
row2 = ["4","5","6"]
row3 = ["7","8","9"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")

liczba = input("podaj liczbe ktore pole chcesz X: ")
col = int(liczba[0])
row = int(liczba[1])

map[col-1][row-1] = "X"
print(f"{row1}\n{row2}\n{row3}")