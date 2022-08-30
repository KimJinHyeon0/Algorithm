def reverse(x):
    if x == 1:
        return 2
    elif x == 2:
        return 1
    elif x == 3:
        return 4
    elif x == 4:
        return 3

def color_check(x, y, d):
    nx, ny = x + dir_l[d][0], y + dir_l[d][1]

    if 0 <= nx < N and 0 <= ny < N:
        return color_map[nx][ny], nx, ny, d
    else:
        return 2, x, y, d

def move(x, y, d, i):
    global result
    color, nx, ny, nd = color_check(x, y, d)
    print(f'{color}, {nx}, {ny}, {nd}')
    if color == 0:
        for n, k in enumerate(table[x][y]): #기존 table에 있던 말들
            horse_l[k] = [nx, ny, horse_l[k][2], len(table[nx][ny]) + n]
        table[nx][ny].extend(table[x][y])
        table[x][y] = []

    elif color == 1:
        for n, k in enumerate(reversed(table[x][y])):
            horse_l[k] = [nx, ny, horse_l[k][2], len(table[nx][ny]) + n]
        table[nx][ny].extend(reversed(table[x][y]))
        table[x][y] = []

    elif color == 2:
        ncolor, nx, ny, nd = color_check(x, y, reverse(d))

        if ncolor == 0:
            for n, k in enumerate(table[x][y]):
                horse_l[k] = [nx, ny, horse_l[k][2], len(table[nx][ny]) + n]
            horse_l[i][2] = nd
            table[nx][ny].extend(table[x][y])
            table[x][y] = []

        elif ncolor == 1:
            for n, k in enumerate(reversed(table[x][y])):
                horse_l[k] = [nx, ny, horse_l[k][2], len(table[nx][ny]) + n]
            horse_l[i][2] = nd
            table[nx][ny].extend(reversed(table[x][y]))
            table[x][y] = []

        elif ncolor == 2:
            horse_l[i] = [x, y, nd, 0]
    if len(table[nx][ny]) >= 4:
        print(result)
        exit()

N, K = map(int, input().split())
color_map = list(list(map(int, input().split())) for _ in range(N)) #map color
table = [[[] for _ in range(N)] for _ in range(N)] # 말의 위치 (index)
horse_l = []
for i in range(K):
    x, y, d = map(int, input().split())
    table[x-1][y-1].append(i)
    horse_l.append([x-1, y-1, d, 0])  # x, y, dir, floor
dir_l = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]

result = 0
while result < 10:
    result += 1
    for i in range(K):
        print(f'{result}, {horse_l}')
        print(f'{result}, {table}')
        (x, y, d, floor) = horse_l[i]
        if floor == 0:
            print(f'move {i}')
            move(x, y, d, i)
            print(f'{result}, {horse_l}')
            print(f'{result}, {table}')
        else:
            continue

print(-1)
