k = int(input())

for i in range (k):
    print(' '*(k-i-1)+'*'*(2*(i+1)-1))

for i in range (k-2,-1,-1):
    print(' '*(k-i-1)+'*'*(2*(i+1)-1))