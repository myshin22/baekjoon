n,x  = map(int, input().split())

a = input()
a_list = list(map(int,a.split()))

b = []

for i in range(n):
    if a_list[i] < x:
        b.append(a_list[i])

print(*b)