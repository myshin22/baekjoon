n = int(input())

li = list(map(int,input().split()))

v = int(input())

num = 0

for i in range(len(li)):
    if li[i] == v:
        num+= 1
   
print(num)