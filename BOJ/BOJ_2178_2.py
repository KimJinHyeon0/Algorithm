def dfs(x, y):
    for i in range(4):
        nx, ny = x+dir_l[i][0], y+dir_l[i][1]
        if 0 <= nx < N and 0 <= ny < M:
            if table[nx][ny] == 1 or table[nx][ny] > table[x][y] + 1:
                table[nx][ny] = table[x][y] + 1
                dfs(nx, ny)

N, M = map(int, input().split())
table = list(list(map(int, input())) for _ in range(N))
dir_l = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dfs(0, 0)
print(table)