from collections import deque

N, K = map(int, input().split())
visited = [-1 for _ in range(100001)]
visited[N]=0
def bfs():
    q = deque()
    q.append(N)
    while q:
        s=q.popleft()
        if s == K:
            return s
        if 0 <= s-1 < 100001 and visited[s-1]==-1:
            visited[s-1]=visited[s]+1
            q.append(s-1)
        if 0 <= s*2 < 100001 and visited[s*2]==-1:
            visited[s*2]=visited[s]
            q.appendleft(s*2)
        if 0 <= s+1 < 100001 and visited[s+1]==-1:
            visited[s+1]=visited[s]+1
            q.append(s+1)

print(visited[bfs()])
