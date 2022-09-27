zero_l = []
table = [[] for _ in range(9)]
for i in range(9):
    tmp = list(map(int, input().split()))
    table[i] = tmp
    for j, k in enumerate(tmp):
        if not k:
            zero_l.append([i, j])
dir_l = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [2, 0], [2, 1], [2, 2]]
n = len(zero_l)
result = [0]

def cand(x, y, t):

    row = table[x]
    column = list(lambda x: table[i][y] for i in range(9))
    cube = list(lambda x: table[(x // 3) * 3 + i][(y // 3) * 3 + j] for i, j in dir_l)

    if len(set(row)) >= len(set(row + [t])) or \
        len(set(column)) >= len(set(column + [t])) or \
        len(set(cube)) >= len(set(cube + [t])):

        return False
    else:
        table[x][y] = t
        return True

def dfs(cnt):
    if cnt == n:
        for t in table:
            print(' '.join(map(str, t)))
        exit()
    else:
        x, y = zero_l[cnt]
        for i in range(1, 10):
            if cand(x, y, i):
                dfs(cnt+1)
                table[x][y] = 0

dfs(0)
