from collections import deque

def dfs():
    q = deque()
    q.append([1, 0])
    while q:
        loc, cnt = q.popleft()

        for i in range(1, 7):
            new = table[loc+i]
            if new > 100:
                continue

            if new == 100:
                return cnt+1
            elif not visited[new]:
                visited[new] = True
                q.append([new, cnt+1])

N, M = map(int, input().split())
table = [i for i in range(101)]
visited = [False] * 101
visited[1] = True
for _ in range(N+M):
    start, end = map(int, input().split())
    table[start] = end

print(dfs())