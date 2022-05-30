import sys

def dfs(v,cnt):
    visited[v] = True
    global result
    if cnt ==5:
        result = 1
    else:
        for e in adj[v]:
            if not(visited[e]):
                cnt += 1
                dfs(e, cnt)
                visited[e] = False
                if result:
                    return


n, m = map(int, sys.stdin.readline().split(' '))
adj = [[] for _ in range(n)]


for _ in range(m):
    x, y = map(int, sys.stdin.readline().split(' '))
    adj[x].append(y)
    adj[y].append(x)

# for e in adj:
#     e.sort()

visited = [False] * (n)
cnt = 1
result = 0

for i in range (n):
    dfs(i, cnt)
    visited[i] = False
    if result:
        break

print(result)