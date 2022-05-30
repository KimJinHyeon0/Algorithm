def DFS(cnt, node, visited):
    global result
    print(node)
    visited[node] = True
    if cnt == 4:
        result = 1
        return

    for x in adj[node]:
        if not visited[x]:
            visited[x] = True
            DFS(cnt+1, x, visited)

N, M = map(int, input().split())
adj = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
print(adj)
result = 0

for i in range(N):
    if result == 0:
        visited = [False] * N
        DFS(0, i, visited)

print(result)