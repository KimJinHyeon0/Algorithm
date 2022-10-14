# 2048 (Easy)

from copy import deepcopy


def show(x):
    for row in x:
        print(*row)
    print('-'*10)


def move(d, mat):
    # print(d)
    if d == 0:   # 상
        for i in range(N):
            p = 0
            x = 0
            for j in range(N):
                if mat[j][i] == 0:
                    continue

                if x == 0:
                    x = mat[j][i]
                else:
                    if x == mat[j][i]:
                        mat[p][i] = x * 2
                        x = 0
                        p += 1
                    else:
                        mat[p][i], x = x, mat[j][i]
                        p += 1

                mat[j][i] = 0

            if x != 0:
                mat[p][i] = x

    elif d == 1:  # 하
        for i in range(N):
            p = N-1
            x = 0

            for j in range(N-1, -1, -1):
                if mat[j][i] == 0:
                    continue
                if x == 0:
                    x = mat[j][i]
                else:
                    if mat[j][i] == x:
                        mat[p][i] = x * 2
                        p -= 1
                        x = 0
                    else:
                        mat[p][i], x = x, mat[j][i]
                        p -= 1
                mat[j][i] = 0
                if x != 0:
                    mat[p][i] = x



    elif d == 2:  # 좌
        for i in range(N):
            p = 0
            x = 0
            for j in range(N):
                if mat[i][j] == 0:
                    continue

                if x == 0:
                    x = mat[i][j]
                else:
                    if x == mat[i][j]:
                        mat[i][p] = x * 2
                        x = 0
                        p += 1
                    else:
                        mat[i][p], x = x, mat[i][j]
                        p += 1

                mat[i][j] = 0

            if x != 0:
                mat[i][p] = x

    elif d == 3:  # 우
        for i in range(N):
            p = N-1
            x = 0
            for j in range(N-1, -1, -1):
                if mat[i][j] == 0:
                    continue

                if x == 0:
                    x = mat[i][j]
                else:
                    if x == mat[i][j]:
                        mat[i][p] = x * 2
                        x = 0
                        p -= 1
                    else:
                        mat[i][p], x = x, mat[i][j]
                        p -= 1

                mat[i][j] = 0

            if x != 0:
                mat[i][p] = x
    # show(mat)
    return mat

def check_max(table):
    global result

    for i in range(N):
        for j in range(N):
            result = max(table[i][j], result)

def dfs(mat, cnt):
    if cnt == 4:
        check_max(mat)
        return

    for i in range(4):
        dfs(move(i, deepcopy(mat)), cnt + 1)


N = int(input())
table = list(list(map(int, input().split())) for _ in range(N))
result = 0
# show(table)
for i in range(4):
    dfs(move(i, deepcopy(table)), 0)
    # move(i, deepcopy(table))
print(result)
