li = []
mx = -1 
loc_max = []

for i in range (9): #행
    li= list((map(int, input().split())))
    for j in range(9): #열
        temp = li[j]
        if temp > mx:
            mx = temp
            loc_max = [i+1,j+1]

print(mx)
print(*loc_max)