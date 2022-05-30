from collections import deque
from copy import deepcopy

def BFS(start):
    global size, cnt, time
    copy = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append(start)
    net = []
    while queue:
        k = queue.popleft()
        for i in range(4):
            nx, ny = k[0] + directions[i][0], k[1] + directions[i][1]
            if 0 <= nx < N and 0 <= ny < N and table[nx][ny] <= size and copy[nx][ny] == 0:
                copy[nx][ny] = copy[k[0]][k[1]] + 1
                queue.append((nx, ny))
                if 0 < table[nx][ny] < size:
                    net += [(copy[nx][ny], nx, ny)]
    if net:
        net.sort()
        dst = net[0]
        time += dst[0]
        cnt += 1
        table[dst[1]][dst[2]] = 0

        if cnt == size:
            size += 1
            cnt = 0

        BFS((dst[1], dst[2]))

N = int(input())
table = list(list(map(int, input().split())) for _ in range(N))
directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
size = 2
cnt = 0
time = 0

for i in range(N):
    for j in range(N):
        if table[i][j] == 9:
            table[i][j] = 0
            start = (i, j)
BFS(start)
print(time)