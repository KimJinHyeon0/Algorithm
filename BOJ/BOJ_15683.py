from itertools import combinations
from copy import deepcopy

def fill(arr, case, x, y):
    for m in case:
        nx, ny = x + dx_l[m], y + dy_l[m]
        while 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0:
                arr[nx][ny] = '#'
            elif arr[nx][ny] == 6:
                break
            nx += dx_l[m]
            ny += dy_l[m]

def DFS(arr, k):
    global result
    copy = deepcopy(arr)

    if k == len(c):
        num = 0
        for i in range(N):
            num += copy[i].count(0)
        result = min(result, num)
        return

    x, y, t = c[k]
    for case in d_class[t]:
        fill(copy, case, x, y)
        DFS(copy, k+1)
        copy = deepcopy(arr)

N, M = map(int, input().split())
table = [[] for _ in range(N)]
c = []
cnt = 0
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        if 0 < temp[j] < 6:
            c.append([i, j, temp[j]])
            cnt += 1
        table[i] = temp

dx_l = [1, 0, -1, 0]
dy_l = [0, 1, 0, -1]
d_class = [[] for _ in range(6)]
d_class[1] = [[0], [1], [2], [3]]
d_class[2] = [[0, 2], [1, 3]]
d_class[3] = [[0, 1], [1, 2], [2, 3], [0, 3]]
d_class[4] = [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]
d_class[5] = [[0, 1, 2, 3]]
result = 100
DFS(table, 0)
print(result)