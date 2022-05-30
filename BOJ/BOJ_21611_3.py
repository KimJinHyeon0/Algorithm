def table2list():
    marble = [0 for _ in range(N**2 - 1)]
    cnt = -1
    p = -1
    x, y = s_x, s_y
    for i in range(1, N):
        for j in range(2):
            cnt = (cnt+1)%4
            for k in range(i):
                if x == s_x and y == s_y:
                    pre_value = 1
                else:
                    pre_value = n_value
                x, y = x+dir_l[cnt][0], y+dir_l[cnt][1]
                n_value = table[x][y]
                if n_value:
                    p += 1
                    marble[p] = n_value
                if not pre_value + n_value:
                    return marble[:p+1]

    cnt = (cnt+1)%4
    for k in range(i):
        pre_value = n_value
        x, y = x+dir_l[cnt][0], y+dir_l[cnt][1]
        n_value = table[x][y]
        if n_value:
            p += 1
            marble[p] = n_value
        if not pre_value + n_value:
            return marble[:p+1]

    return marble[:p+1]

def list2table():
    new_table = [[0 for _ in range(N)] for _ in range(N)]

    cnt = -1
    p = -1
    x, y = s_x, s_y
    for i in range(1, N):
        for j in range(2):
            cnt = (cnt+1)%4
            for k in range(i):
                p += 1
                x, y = x + dir_l[cnt][0], y + dir_l[cnt][1]
                new_table[x][y] = marble[p]
                if p == len(marble) - 1:
                    return new_table
    return new_table


def ice(t):
    x, y = N // 2, N // 2
    dir, cnt = magic[t]
    for i in range(cnt):
        x, y = x+ex_dir_l[dir][0], y+ex_dir_l[dir][1]
        table[x][y] = 0

def bingo():
    global result
    if not marble: return
    recur = True
    while recur:
        indices, value = [], -1
        remove_indices = []
        recur = False
        for i in range(len(marble)):
            if value == 0:
                break
            if marble[i] == value:
                indices.append(i)
            else:
                if len(indices) >= 4:
                    recur = True
                    remove_indices.extend(indices)
                    result += value*len(indices)
                indices, value = [i], marble[i]
        for k in sorted(remove_indices, reverse=True):
            marble.pop(k)

def change():
    new_marble = []
    if not marble: return new_marble
    group = [1, marble[0]]
    for i in range(1, len(marble)):
        if marble[i] == group[1]:
            group[0] += 1
        else:
            new_marble.extend(group)
            group = [1, marble[i]]
    new_marble.extend(group)
    return new_marble

N, M = map(int, input().split())
table = list(list(map(int, input().split())) for _ in range(N))
magic = list(list(map(int, input().split())) for _ in range(M))
dir_l = [[0, -1], [1, 0], [0, 1], [-1, 0]]
ex_dir_l = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]
result = 0
s_x, s_y = N//2, N//2
for i in range(M):
    ice(i)
    marble = table2list()
    bingo()
    table = list2table()
    marble = change()
    table = list2table()
print(result)