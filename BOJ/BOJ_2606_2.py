import sys
from collections import deque

input = lambda : sys.stdin.readline()

N = int(input())
M = int(input())
g = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    g[a][b] = -1
    g[b][a] = -1

infected = [0] * (N+1)
list = deque(g[1])

def is_valid(list):
    if list:
        node = list.popleft()
    else:
        node = 0
    return node

node = is_valid(list)

while node:
    infected[node] = 1
    list.extend(g[node])
    node = is_valid(list)

print(sum(infected))