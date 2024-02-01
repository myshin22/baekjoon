prior = ['c=','c-','dz=','d-','lj','nj','s=','z=']

user =input()

num = 0 

for i in prior:
    user = user.replace(i, "x")

print(len(user))