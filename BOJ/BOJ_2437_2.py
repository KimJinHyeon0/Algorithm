import sys
from itertools import permutations

input = lambda : sys.stdin.readline()

N = int(input())
weight = sorted(list(map(int, input().split())))

min = 1

for i in range(N):
    if weight[i] > min:
        break
    min += weight[i]
print(min)
