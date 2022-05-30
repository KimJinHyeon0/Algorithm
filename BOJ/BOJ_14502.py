from collections import deque
from copy import deepcopy
from itertools import combinations

def BFS(cnt):
    while queue:
        k = queue.popleft()
        for i in range(4):
            nx, ny = k[0] + directions[i][0], k[1] + directions[i][1]
            if (0 <= nx < N) and (0 <= ny < M) and copy[nx][ny] == 0:
                copy[nx][ny] = 2
                queue.append((nx, ny))
                cnt += 1
    return cnt

N, M = map(int, input().split())

table = list(list(map(int, input().split())) for _ in range(N))
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
answer = 0
virus = []
available = []
wall = 0
for i in range(N):
    for j in range(M):
        if table[i][j] == 2:
            virus.append((i, j))
        elif table[i][j] == 0:
            available.append((i, j))
        else:
            wall += 1

for case in combinations(available, 3):
    cnt = len(virus)
    queue = deque(virus)
    copy = deepcopy(table)
    for p in case:
        copy[p[0]][p[1]] = 1
    answer = max(answer, (N*M - (wall + 3) - BFS(cnt)))

print(answer)

