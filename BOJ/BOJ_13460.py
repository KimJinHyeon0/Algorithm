from collections import deque

def move(x, y, dx, dy, c):
    while table[x + dx][y + dy] != '#' and table[x][y] != 'O':
        x += dx
        y += dy
        c += 1
    return x, y, c

def BFS(rx, ry, bx, by):
    global result
    queue = deque()
    queue.append((rx, ry, bx, by, 1))

    while queue:
        rx, ry, bx, by, d = queue.popleft()
        if d > 10:
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, d_l[i][0], d_l[i][1], d)
            nbx, nby, bc = move(bx, by, d_l[i][0], d_l[i][1], d)

            if table[nbx][nby] != 'O':
                if table[nrx][nry] == 'O':
                    answer = d
                    return
                if (nrx, nry) == (nbx, nby):
                    if rc > bc:
                        nrx -= d_l[i][0]
                        nry -= d_l[i][1]
                    else:
                        nbx -= d_l[i][0]
                        nby -= d_l[i][1]

                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby, d+1))

N, M = map(int, input().split())
table = list(list(map(str, input())) for _ in range(N))
d_l = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(N):
    for j in range(M):
        if table[i][j] == 'R':
            rx, ry = i, j
        elif table[i][j] == 'B':
            bx, by = i, j
        elif table[i][j] == 'O':
            ox, oy = i, j

visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
visited[rx][ry][bx][by] = True
result = -1
BFS(rx, ry, bx, by)
print(result)