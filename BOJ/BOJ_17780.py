N, K = map(int, input().split())
table = list(list(map(int, input().split())) for _ in range(N))
rock_table = [[[] for _ in range(N)] for _ in range(N)]
rock_l = [[] for _ in range(K)]
for i in range(K):
    x, y, d = map(int, input().split())
    rock_l[i] = [x-1, y-1, d]
    rock_table[x-1][y-1] = [[i]]
dir_l = [[], [-1, 0], [1, 0], [0, -1], [0, 1]]
result = -1

for index, x, y, d in enumerate(rock_l):
    if rock_table[x][y][0] != index:
        continue
    nx, ny = x+dir_l[d][0], y+dir_l[d][1]
    if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:

    if table[nx][ny] < 2:#white
        rock_table[nx][ny].extend(rock_table[x][y])
        rock_table[x][y] = []
        if table[nx][ny] == 1: #red
            rock_table[nx][ny].reverse()
    else: #blue
        if d == 1:
            k = 2
        elif d == 2:
            k = 1
        elif d == 3:
            k = 4
        else:
            k = 3
        nx, ny = x+dir_l[k][0], y+dir_l[k][1]




