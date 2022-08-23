row1 = ["1","2","3"]
row2 = ["4","5","6"]
row3 = ["7","8","9"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")

number = input("Give number to choose X coordinate: ")
col = int(number[0])
row = int(number[1])

map[col-1][row-1] = "X"
print(f"{row1}\n{row2}\n{row3}")
