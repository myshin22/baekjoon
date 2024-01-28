t = int(input())
new_s =''

for i in range (t):
    new_s =''
    r, s = input().split()
    
    
    for i in range (len(s)):
        temp = s[i] *int(r)
        new_s += temp
        
    print(new_s)