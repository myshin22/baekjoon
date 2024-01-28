
n,m = map(int, input().split())

li = [i+1 for i in range (n)]
    
for i in range(m):
    a,b = map(int, input().split())
    li_2 = list(reversed(li[a-1: b]))
    k = -1
    for j in range(a-1,b):
        k += 1
        li[j] = li_2[k]
    

print(*li)