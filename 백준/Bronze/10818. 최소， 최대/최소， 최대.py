n = int(input())
x = input()
x_list = list(map(int, x.split()))

max_x = max(x_list)
min_x = min(x_list)

min_max_x = []
min_max_x.append(min_x)
min_max_x.append(max_x)

print(*min_max_x)
    