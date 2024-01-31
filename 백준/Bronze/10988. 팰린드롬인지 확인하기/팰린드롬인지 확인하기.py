word = list(input())
a=1

for i in range (len(word)//2):
    if (word[i] != word[-(i+1)]):
        a = 0
        break

print(a)