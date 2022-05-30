import sys
from math import ceil
input = lambda : sys.stdin.readline()

N = int(input())

A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for x in A:
    if x - B <= 0:
        answer += 1
    else:
        answer += ceil((x - B) / C) + 1

print(answer)