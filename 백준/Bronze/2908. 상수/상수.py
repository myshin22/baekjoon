a,b = input().split()

a_list = list(reversed(list(a)))
b_list = list(reversed(list(b)))

a = ''.join(a_list)
b = ''.join(b_list)

if int(a) > int(b):
    print(int(a))
else:
    print(int(b))