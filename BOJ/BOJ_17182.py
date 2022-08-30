N, K = map(int, input().split())
time = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
visited[K] = True
result = 1e4

for k in range(N):
    for i in range(N):
        for j in range(N):
            time[i][j] = min(time[i][j], time[i][k] + time[k][j])

def dfs(x, t, cnt):
    global result
    if N == cnt:
        result = min(result, t)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(i, t + time[x][i], cnt+1)
            visited[i] = False

dfs(K, 0, 1)
print(result)