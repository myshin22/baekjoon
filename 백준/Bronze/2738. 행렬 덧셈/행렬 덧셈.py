n,m = map(int, input().split())

li =[]
li_2 =[]
li_sum =[]

for i in range(n):
    li.extend(map(int, input().split()))

for i in range(n):
    li_2.extend(map(int, input().split()))

for i in range(n*m):
    li_sum.append(li[i]+li_2[i])

for i in range(n):
   print(*li_sum[i*m:i*m+m])