from collections import deque

def BFS(table):
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if table[nx][ny] == 1:
                    queue.append((nx, ny))
                    table[nx][ny] += table[x][y]


N, M = map(int, input().split())
table = list(list(map(int, input())) for _ in range(N))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

BFS(table)

print(table)