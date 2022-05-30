import sys
from collections import deque

input = lambda :sys.stdin.readline()

dx = (2, 1, -1, -2, -2, -1, 1, 2)
dy = (1, 2, 2, 1, -1, -2, -2, -1)

def bfs():
    q = deque()
    q.append((start_x, start_y))
    while q:
        x, y = q.popleft()
        if x == dst_x and y == dst_y:
            print(d[x][y])
            return
        for i in range(8):
            next_x, next_y = x+dx[i], y+dy[i]
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
                continue
            if not d[next_x][next_y]:
                d[next_x][next_y] = d[x][y] + 1
                q.append((next_x, next_y))

for _ in range(int(input())):
    n = int(input())
    start_x, start_y = map(int, input().split())
    dst_x, dst_y = map(int, input().split())
    d = [[0]*n for _ in range(n)]
    bfs()
