import sys
from collections import Counter
from math import ceil
input = lambda : sys.stdin.readline()


T = int(input())


# for _ in range(T):
#     N, K = map(int, input().split())
#     S = list(map(str, input().rstrip()))


N, K = 5, 1
S = ['B', 'B', 'B', 'B', 'B']

S = list(map(int, list(x.replace('A', '1').replace('B', '-1') for x in S)))

for x in S:
