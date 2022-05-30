import sys
from bisect import bisect_left

input = lambda: sys.stdin.readline()

n = int(input())
port_list = list(map(int, input().split()))
lis = []

for port in port_list:
    if not lis:
        lis.append(port)
        continue
    if lis[-1] < port:
        lis.append(port)
    else:
        index = bisect_left(lis, port)
        lis[index] = port
print(len(lis))