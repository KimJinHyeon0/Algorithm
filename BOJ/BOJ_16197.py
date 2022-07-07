N, M = map(int, input().split())
coin_l = []
table = [[] for _ in range(N)]
coin_map = [[100]*M for _ in range(N)]

for i in range(N):
    tmp = list(map(str, input()))
    for j, k in enumerate(tmp):
        if k == 'o':
            coin_l.append([i, j])
            coin_map[i][j] = 0
    table[i] = tmp

dir_l = [[1, 0], [0, 1], [-1, 0], [0, -1]]

result = 100
def bfs(cnt, a, b, k):
    global result
    if cnt > 10:
        return
    tmp = []
    nax, nay = a[0] + dir_l[k][0], a[1] + dir_l[k][1]
    nbx, nby = b[0] + dir_l[k][0], b[1] + dir_l[k][1]

    if 0 <= nax < N and 0 <= nay < M:
        if table[nax][nay] != '#':
            coin_map[nax][nay] = min(coin_map[a[0]][a[1]] + 1, cnt)
        else:
            nax, nay = a[0], a[1]
    else:
        tmp.append(cnt)

    if 0 <= nbx < N and 0 <= nby < M:
        if table[nbx][nby] != '#':
            coin_map[nbx][nby] = min(coin_map[b[0]][b[1]] + 1, cnt)
        else:
            nbx, nby = b[0], b[1]
    else:
        tmp.append(cnt)

    if abs(nax - nbx) + abs(nay - nby) > 0:
        if len(tmp) > 0:
            if len(tmp) == 1:
                result = min(result, tmp[0])
            return

        for i in range(4):
            bfs(cnt+1, [nax, nay], [nbx, nby], i)

for i in range(4):
    bfs(1, coin_l[0], coin_l[1], i)

if result == 100:
    print(-1)
else:
    print(result)