from copy import deepcopy

def add():
    indices, value = [], 10001
    temp = table[-1]
    for i, k in enumerate(temp):
        if k < value:
            indices = [i]
            value = k
        elif k == value:
            indices.append(i)

    for i in indices:
        table[-1][i] = value+1

def cycle():
    start_i, end_i = 0, 0
    cnt = 2
    while True:
        step = cnt//2
        start_j = (cnt + 1) // 2
        start_i = end_i
        end_i += step
        if start_j > N - end_i:
            break
        for x, i in enumerate(range(start_i, end_i)):
            for y, j in enumerate(range(-1, -start_j-1, -1)):
                table[-1-step+x][end_i+y] = table[j][i]
                table[j][i] = 0
        cnt += 1
    return start_i

def calib():
    temp_table = deepcopy(table)
    for i in range(N):
        for j in range(N):
            if table[i][j]:
                if i+1 < N and table[i+1][j]:
                    if table[i][j] > table[i+1][j]:
                        diff = (table[i][j] - table[i+1][j])//5
                        temp_table[i][j] -= diff
                        temp_table[i+1][j] += diff
                    else:
                        diff = (table[i+1][j] - table[i][j])//5
                        temp_table[i][j] += diff
                        temp_table[i+1][j] -= diff

                if j+1 < N and table[i][j+1]:
                    if table[i][j] > table[i][j+1]:
                        diff = (table[i][j] - table[i][j+1])//5
                        temp_table[i][j] -= diff
                        temp_table[i][j+1] += diff
                    else:
                        diff = (table[i][j+1] - table[i][j])//5
                        temp_table[i][j] += diff
                        temp_table[i][j+1] -= diff

    return temp_table

def flatten(idx):
    temp = []
    for i in range(idx, N):
        for j in range(-1, -N-1, -1):
            if table[j][i]:
                temp.append(table[j][i])
                table[j][i] = 0
    table[-1] = temp




def half():
    start_i, end_i = 0, N//2
    temp = table[-1][: end_i]
    table[-1][:end_i] = [0] * end_i
    temp.reverse()
    table[-2][end_i:] = temp

    start_i = end_i
    end_i += N//4
    for x, y in zip([-1, -2], [-4, -3]):
        temp = table[x][start_i:end_i]
        table[x][start_i:end_i] = [0] * (N//4)
        temp.reverse()
        table[y][end_i:] = temp

    return end_i

N, K = map(int, input().split())
table = [[0] * N for _ in range(N)]
table[-1] = list(map(int, input().split()))
result = 0
while True:
    add()
    idx = cycle()
    table = calib()
    flatten(idx)
    idx = half()
    table = calib()
    flatten(idx)
    result += 1
    if max(table[-1]) - min(table[-1]) <= K:
        break
print(result)
