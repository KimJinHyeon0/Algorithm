from collections import deque

def BFS(start):
    global united_num

    nations.append([population[start[0]][start[1]], (start)])
    united[start[0]][start[1]] = united_num
    queue = deque()
    queue.append(start)
    while queue:
        k = queue.popleft()
        for i in range(4):
            nx, ny = k[0] + d[i][0], k[1] + d[i][1]
            if 0 <= nx < N and 0 <= ny < N and united[nx][ny] == 0:
                if L <= abs(population[nx][ny] - population[k[0]][k[1]]) <= R:
                    united[nx][ny] = united_num
                    nations[-1].append((nx, ny))
                    nations[-1][0] += population[nx][ny]
                    queue.append((nx, ny))

    united_num += 1

N, L, R = map(int, input().split())
population = list(list(map(int, input().split())) for _ in range(N))
d = [[0, 1], [1, 0], [-1, 0], [0, -1]]
day = 0
while True:
    united_num = 1
    united = [[0 for _ in range(N)] for _ in range(N)]
    nations = [[]]
    start = ()

    for i in range(N):
        for j in range(N):
            if not united[i][j] and len(nations) == united_num:
                start = (i, j)
                BFS(start)
    if len(nations) != (N**2 + 1):
        for i in range(1, len(nations)):
            temp = nations[i][0] // (len(nations[i]) - 1)
            for case in nations[i][1:]:
                population[case[0]][case[1]] = temp

        day += 1

    else:
        break

print(day)

