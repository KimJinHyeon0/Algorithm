import sys

input = lambda : sys.stdin.readline()

N = int(input())

T, P = [0 for _ in range(N)], [0 for _ in range(N)]

for i in range(N):
    temp = list(map(int, input().split()))
    T[i], P[i] = temp[0], temp[1]

dp = [[0, 0] for _ in range(N)]