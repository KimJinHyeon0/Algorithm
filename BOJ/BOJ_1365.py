import sys
from bisect import bisect_left

input = lambda :sys.stdin.readline()

N = int(input())
lines = list(map(int, input().split()))
lis = []

for line in lines:
    if not lis:
        lis.append(line)
        continue
    if lis[-1] < line:
        lis.append(line)
    else:
        index = bisect_left(lis, line)
        lis[index] = line
print(N - len(lis))