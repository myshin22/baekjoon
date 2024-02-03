# 색종이 10*10
# 도화지 100*100

page = [[0 for i in range(100)] for i in range (100)]


num = int(input())

for i in range (num):
    a,b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            page[a+i][b+j] = 1

total = 0 

for i in range (100):
    for j in range(100):
        if page[i][j] == 1:
            total += 1

print(total)