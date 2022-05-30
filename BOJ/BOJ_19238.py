from collections import deque
from copy import deepcopy

def BFS(start, mode, dst):
    global gas
    copy = deepcopy(table)
    copy[start[0]][start[1]] = 0
    queue = deque()
    queue.append(start)
    while queue and d_pass and gas:
        k = queue.popleft()
        for i in range(5):
            nx, ny = k[0] + directions[i][0], k[1] + directions[i][1]
            if 0 <= nx < N and 0 <= ny < N and copy[nx][ny] == 0:
                if nx == k[0] and ny == k[1]:
                    copy[nx][ny] = copy[k[0]][k[1]]
                else:
                    copy[nx][ny] = copy[k[0]][k[1]] + 1
                if mode and [nx, ny] in s_pass:
                    gas -= (copy[nx][ny])
                    if gas <= 0:
                        break
                    idx = s_pass.index([nx, ny])
                    del s_pass[idx]
                    BFS((nx, ny), 0, d_pass[idx])

                elif not mode and dst == [nx, ny]:
                    gas -= (copy[nx][ny])
                    if gas < 0:
                        break
                    gas += 2*(copy[nx][ny])
                    d_pass.remove([nx, ny])
                    BFS((nx, ny), 1, [])
                else:
                    queue.append((nx, ny))

N, M, gas = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
start = list(map(int, input().split()))
start = tuple(map(lambda x: x-1, start))
s_pass = [[]for _ in range(M)]
d_pass = [[]for _ in range(M)]

for i in range(M):
    temp = list(map(int, input().split()))
    s_pass[i], d_pass[i] = list(map(lambda x: x-1, temp[:2])), list(map(lambda x: x-1, temp[2:]))

directions = [(0, 0), (-1, 0), (0, -1), (0, 1), (1, 0)]
mode, dst = 1, [] #mode_1 = find passenger, mode_0 = drop passenger
BFS(start, mode, dst)

if d_pass or gas < 0:
    print(-1)
else:
    print(gas)