def dfs(x, y, d, k):
    global visited
    if k == 0:
        return
    for move in dir_wind[d]:
        nx, ny = x+move[0], y+move[1]
        if 0 <= nx < R and 0 <= ny < R and not visited[nx][ny]:



def wind():
    for x, y, d in fan_l:
        visited = [[0] * R for _ in range(R)]
        dx, dy = 0, 0
        for k in dir_wind[d]:
            dx += k[0]
            dy += k[1]
        dx //=3
        dy //=3

        nx, ny = x+dx, y+dy
        visited[nx][ny] += 5
        for k in range(4, 0, -1):
            print(k)






R, C, K = map(int, input().split())
table = [[] for _ in range(R)]
watch_l = []
fan_l = []
for i in range(R):
    temp = list(map(int, input().split()))
    for j in range(R):
        if 0 < temp[j] < 5:
            fan_l.append([i, j, temp[j]])
            temp[j] = 0
        elif temp[j] == 5:
            watch_l.append([i, j])
            temp[j] = 0

    table[i] = temp
W = int(input())
wall_l = list(list(map(int, input().split())) for _ in range(W))
dir_wind = [[],
            [[-1, 1], [0, 1], [1, 1]],
            [[-1, -1], [0, -1], [1, -1]],
            [[-1, -1], [-1, 0], [-1, 1]],
            [[1, -1], [1, 0], [1, 1]]]

wind()