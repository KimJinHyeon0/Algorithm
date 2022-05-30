import sys

def cal(a):
    if a == 1:
        return 1
    if a == 2:
        return 2
    if a == 3:
        return 4
    else:
        return cal(n-1) + cal(n-2) + cal(n-3)

n = int(input())
for i in range(n):
    data = int(input())
    print(cal(data))