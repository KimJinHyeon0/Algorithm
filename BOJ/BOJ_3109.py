def dfs(x, y):
    if y == C-1:
        return True

    for k in range(3):
        nx, ny = x + dir_l[k], y + 1
        if 0 <= nx < R and 0 <= ny < C and table[nx][ny] == '.' and not visited[nx][ny]:
            visited[nx][ny] = True
            if dfs(nx, ny):
                return True
    return False

R, C = map(int, input().split())
table = list(list(map(str, input())) for _ in range(R))
visited = [[False] * C for _ in range(R)]
dir_l = [-1, 0, 1]
result = 0

for i in range(R-1, -1, -1):
    if table[i][0] == '.':
        if dfs(i, 0):
            result += 1
print(result)