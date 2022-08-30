from collections import deque

max_u = 1e10

def bfs(x, k):
    result = 0
    visited = [False] * (N+1)
    visited[x] = True
    q = deque()
    q.append((x, max_u))

    while q:
        i, min_usa = q.pop()
        for index, usa in enumerate(g[i]):
            if usa >= k and not visited[index]:
                visited[index] = True
                result += 1
                q.append((index, min_usa))
    return result





N, Q = map(int, input().split())
g = [[0] * (N+1) for _ in range(N+1)]

for i in range(N-1):
    p, q, r = map(int, input().split())
    g[p][q] = r
    g[q][p] = r

for i in range(Q):
    k, v = map(int, input().split())
    print(bfs(v, k))
