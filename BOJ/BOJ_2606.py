from collections import deque

def BFS():
    queue = deque()
    queue.append(1)
    while queue:
        k = queue.pop()
        if not visited[k]:
            visited[k] = True
            for x in adj[k]:
                queue.append(x)
    print(sum(visited) - 1)

def DFS(v):
    visited[v] = True
    for x in adj[v]:
        if not visited[x]:
            DFS(x)

n = int(input())
e = int(input())
edges = list(list(map(int, input().split())) for _ in range(e))

adj = [[] for _ in range(n+1)]
for edge in edges:
    adj[edge[0]].append(edge[1])
    adj[edge[1]].append(edge[0])

visited = [False for _ in range(n+1)]

# BFS()
DFS(1)
print(sum(visited)-1)

