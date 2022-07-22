R, C = map(int, input().split())
data = list(list(map(ord, input())) for _ in range(R))
visited = set()
dir_l = [[1, 0], [-1, 0], [0, 1], [0, -1]]
result = 1

def dfs(cnt, x, y):
    global result
    visited.add(data[x][y])

    for i in range(4):
        nx, ny = x + dir_l[i][0], y + dir_l[i][1]
        if 0 <= nx < R and 0 <= ny < C and data[nx][ny] not in visited:
            dfs(cnt+1, nx, ny)
            result = max(result, cnt)
            visited.remove(data[nx][ny])

dfs(1, 0, 0)
print(result)