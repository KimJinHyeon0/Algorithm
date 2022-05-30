import sys
from bisect import bisect_left

input = lambda : sys.stdin.readline()

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(list(map(int, input().split())))
    cnt = 0

    for num in A:
        index = bisect_left(B, num)
        cnt += index
    print(cnt)