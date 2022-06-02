k = int(input())
double_hex = [0] * 12
max_height = 0
max_width = 0

for i in range(6):
    tmp = list(map(int, input().split()))
    if tmp[0] <= 2:
        max_width = max(tmp[1], max_width)
    else:
        max_height = max(tmp[1], max_height)
    double_hex[i], double_hex[i+6] = tmp, tmp

result = max_height * max_width
for i in range(12):
    if double_hex[i][0] == double_hex[i+2][0]:
        if double_hex[i+1][0] == double_hex[i+3][0]:
            result -= double_hex[i+1][1]*double_hex[i+2][1]
            break
print(result*k)