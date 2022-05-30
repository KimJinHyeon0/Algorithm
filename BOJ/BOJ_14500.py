from itertools import product
from copy import deepcopy

def check(m, n):
    if

def DFS(arr, k):
    global result
    if k == 6:
        temp = 0
        for x in range(M):
            for y in range(N):
                temp += arr[x][y] * table[x][y]
        result = max(result, temp)

    for i in range(N):
        for j in range(M):
            for case in shape[k]:
                copy = deepcopy(arr)
                nx, ny, m = i, j, 0
                while 0 <= nx < N and 0 < ny < M and copy[nx][ny]:
                    copy[nx][ny] = 1
                    nx, ny = i + dx_l[case[m]], j + dy_l[case[m]]
                    m += 1
                if m == 3:
                    DFS(copy, k+1)

N, M = map(int, input().split())
table = list(list(map(int, input().split())) for _ in range(N))

dx_l = [0, 1, 0, -1]
dy_l = [1, 0, -1, 0]

check_l = [[1, 0, -1], [1, 0, -1]]
check_list = list(product(*check_l))

shape = [[]for _ in range(5)]
shape[0] = [(0, 0, 0)]
shape[1] = [(0, 0, 1), (0, 0, 3)]
shape[2] = [(0, 1, 0), (0, 3, 0)]
shape[3] = [(0, 1, 2)]
shape[4] = [(0, 3, 2)]
for i in range(5):
    for _ in range(8):
        if 0 < i < 3:
            shape[i].append(tuple(map(lambda x: (x + 1) % 4, shape[i][-2])))
        else:
            shape[i].append(tuple(map(lambda x: (x + 1) % 4, shape[i][-1])))
    shape[i] = list(set(shape[i]))

empty = [[0 for _ in range(N)] for _ in range(M)]
result = 2000
DFS(empty, 0)