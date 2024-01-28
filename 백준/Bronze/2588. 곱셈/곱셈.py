A = int(input())
B = int(input())

B_1 = B // 100
B_2 = (B // 10) % 10 
B_3 = B % 10 

output1 = A * B_1
output2 = A * B_2
output3 = A * B_3
output4 = A * B

print(output3)
print(output2)
print(output1)
print(output4)