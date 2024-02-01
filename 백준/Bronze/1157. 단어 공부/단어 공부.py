word = list(input())


li_output = [0 for i in range(26)]

for i in range(len(word)):
    x = ord(word[i])
    if  65 <= x <= 90:
        li_output[x-65]+= 1
    else:
        li_output[x-97]+=1

pos = [i for i in range(len(li_output)) if li_output[i]== max(li_output)]

if len(pos) == 1:
    print(chr(pos[0]+65))
else:
    print('?')