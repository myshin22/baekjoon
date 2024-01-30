li = [1,1,2,2,2,8]

li_input=list(input().split())
li_output = []

for i in range(6):
    li_output. append(int(li[i]) - int(li_input[i])) 

print(*li_output)