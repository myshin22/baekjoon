li=[0 for i in range (42)]

for i in range(10):
    x = int(input()) % 42
    li[x] = 1

num = 0

for i in range(42):
    if li[i] == 1:
        num += 1

print(num)