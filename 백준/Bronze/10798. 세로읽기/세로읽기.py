row =[]
max = -1

for i in range(5): #행
    temp = input()
    if len(temp) > max:
        max = len(temp)
    row.append(temp)


for j in range(max):
    for i in range(len(row)):
        if len(row[i]) > j:
            print(row[i][j], end="")
