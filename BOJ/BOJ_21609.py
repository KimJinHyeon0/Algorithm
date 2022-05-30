def find_group(value, temp, x, y):
    global target_group

    for k in range(4):
        nx, ny = x+dir_l[k][0], y+dir_l[k][1]

        if 0 <= nx < N and 0 <= ny < N and table[nx][ny] >= 0 and \
                [nx, ny] not in temp[1] and [nx, ny] not in temp[2]:
            n_value = table[nx][ny]
            if n_value == 0:
                temp[0] += 1
                temp[1] += [[nx, ny]]
                find_group(value, temp, nx, ny)
            else:
                if value == 0:
                    temp[0] += 1
                    temp[2] += [[nx, ny]]
                    find_group(n_value, temp, nx, ny)
                elif value == n_value:
                    temp[0] += 1
                    temp[2] += [[nx, ny]]
                    find_group(value, temp, nx, ny)

    if temp[0] >= 2 and len(temp[2]) > 0:
        if target_group[0] < temp[0]:
            temp[2].sort()
            target_group = temp
        elif target_group[0] == temp[0]:
            temp[2].sort()
            if target_group[2][0] < temp[2][0]:
                target_group = temp




N, M = map(int, input().split())
table = [[] for _ in range(N)]
score = 0
rainbow_l = []
for i in range(N):
    temp = list(map(int, input().split()))
    table[i] = temp
    for j in range(N):
        if temp[j] == 0:
            rainbow_l.append([i, j])

dir_l = [[0, 1], [0, -1], [1, 0], [-1, 0]]
while True:
    target_group = [0, [], []]
    for i in range(N):
        for j in range(N):
            if table[i][j] > 0:
                find_group(table[i][j],[1, [], [[i, j]]], i, j) #temp = [#block, rainbow_l, normal_l]
            elif table[i][j] == 0:
                find_group(table[i][j],[1, [[i, j]], []], i, j) #temp = [#block, rainbow_l, normal_l]

    print(target_group)
    if not target_group[0]:
        break
    score += (target_group[0])**2

    exit()