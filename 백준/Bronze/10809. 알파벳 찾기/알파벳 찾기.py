s = input()
len_s = len(s)

#아스키 코드 97부터 122
li =[-1 for i in range (26)]

for i in range (len_s):
    aski_s = ord(s[i])
    if li[aski_s - 97] == -1:
        li[aski_s -97] = i


print(*li)
