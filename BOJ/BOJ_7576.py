from collections import deque

def BFS():
    global day, pm
    while queue:
        for t in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dir_l[i][0]
                ny = y + dir_l[i][1]
                if 0 <= nx < N and 0 <= ny < M and not table[nx][ny]:
                    table[nx][ny] = 1
                    queue.append((nx, ny))
                    pm -= 1
        day += 1

M, N = map(int, input().split())
table = list(list(map(int, input().split())) for _ in range(N))
dir_l = [[1, 0], [0, 1], [-1, 0], [0, -1]]
queue = deque()
block = 0
day = -1
for i in range(N):
    for j in range(M):
        if table[i][j] == 1:
            queue.append((i, j))
        elif table[i][j] == -1:
            block += 1

pm = (M*N) - block - len(queue)
if not pm:
    print(0)

else:
    BFS()
    if pm != 0:
        print(-1)
    else:
        print(day)
