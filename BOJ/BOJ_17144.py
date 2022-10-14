# 미세먼지 안녕!

from copy import deepcopy


def show(x):
    for row in x:
        print(*row)

    print('-'*20)


def spread():
    temp_table = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if table[i][j] > 0:
                tot_dust = table[i][j]
                div_dust = tot_dust // 5
                cnt = 0
                for d in range(4):
                    ni, nj = i + dir_l[d][0], j + dir_l[d][1]
                    if 0 <= ni < R and 0 <= nj < C and table[ni][nj] != -1:
                        temp_table[ni][nj] += div_dust
                        cnt += 1
                temp_table[i][j] -= (div_dust * cnt)

    for i in range(R):
        for j in range(C):
            table[i][j] += temp_table[i][j]

def define_wind_map(clockwise):
    wind_map = []

    if clockwise == True:
        x, y = downer_cleaner
        nx, ny = x, y
        for i in range(4):
            while x <= nx < R and 0 <= ny < C:
                wind_map.append((nx, ny))
                nx += dir_l[i][0]
                ny += dir_l[i][1]
            nx -= dir_l[i][0]
            ny -= dir_l[i][1]
            wind_map = wind_map[:-1]

    if clockwise == False:
        x, y = upper_cleaner
        nx, ny = x, y
        for i in range(2, -2, -1):
            while 0 <= nx <= x and 0 <= ny < C:
                wind_map.append((nx, ny))
                nx += dir_l[i][0]
                ny += dir_l[i][1]
            nx -= dir_l[i][0]
            ny -= dir_l[i][1]
            wind_map = wind_map[:-1]

    # wind_map = [[before], [after]]
    wind_map = [wind_map for _ in range(2)]
    wind_map[0] = wind_map[0][1:] + [wind_map[0][0]]
    return wind_map


def wind():
    for before, after in zip(upper_wind_map[0], upper_wind_map[1]):
        bx, by = before
        ax, ay = after
        if table[bx][by] == -1:
            continue
        # print(f'{bx, by} -> {ax, ay}')
        if table[ax][ay] != -1:
            table[ax][ay] = table[bx][by]
        table[bx][by] = 0
    for before, after in zip(downer_wind_map[0], downer_wind_map[1]):
        bx, by = before
        ax, ay = after
        if table[bx][by] == -1:
            continue
        # print(f'{bx, by} -> {ax, ay}')
        if table[ax][ay] != -1:
            table[ax][ay] = table[bx][by]
        table[bx][by] = 0


def score():
    result = 0
    for i in range(R):
        for j in range(C):
            if table[i][j] > 0:
                result += table[i][j]
    return result
R, C, T = map(int, input().split())
table = [[] for _ in range(R)]
dir_l = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # counter-clockwise
upper_cleaner = []
downer_cleaner = []

for i in range(R):
    tmp = list(map(int, input().split()))
    for j in range(C):
        if tmp[j] == -1:
            if not upper_cleaner:
                upper_cleaner = [i, j]
            else:
                downer_cleaner = [i, j]
    table[i] = tmp

# show(table)

upper_wind_map = define_wind_map(False)
downer_wind_map = define_wind_map(True)
for t in range(T):
    spread()
    wind()
# show(table)
print(score())