n,m = map(int, input().split())

li = [0 for i in range(n)]

for i in range(m):
    start, end, num = map(int, input().split())
    for j in range(start-1,end):
        li[j] = num

print(*li)
