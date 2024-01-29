# 숫자 1은 2초 2는 3초...9는 10초 

dial = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]


# a == 65, z ==90
user = input()
input_user = list(user)

sum = 0

for i in range(len(user)):
   sum += dial[ord(input_user[i]) -65]+1

print(sum)

