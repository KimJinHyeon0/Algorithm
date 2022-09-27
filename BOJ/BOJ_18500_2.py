import sys
sys.setrecursionlimit(10**6)
def show(matrix):
    for row in matrix:
        print(''.join(row))
def check(i, x):
    dir = i%2
    if dir == 0:
        k = 0
        while k < C and table[R - x][k] == '.':
            if k == C-1:
                break
            k += two_dir_l[dir]
    elif dir == 1:
        k = C-1
        while 0 <= k and table[R - x][k] == '.':
            if k == 0:
                break
            k += two_dir_l[dir]

    if table[R-x][k] == 'x':
        return True, R-x, k
    else:
        return False, R - x, k

def break_mineral(x, y):
    table[x][y] = '.'

def dfs(x, y):
    global recur

    if x == R-1 or not recur:
        recur = False
        return

    visited[x][y] = 1
    cand.append([x, y])
    for i in range(4):
        nx, ny = x + dir_l[i][0], y + dir_l[i][1]
        if 0 <= nx < R and 0 <= ny < C and table[nx][ny] == 'x' and not visited[nx][ny]:
            dfs(nx, ny)

def fall(l):
    step = 100
    l.sort(key=lambda x: x[0], reverse=True)
    for x, y in l:
        k = 1
        while x + k < R:
            if visited[x+k][y]:
                break
            elif table[x+k][y] == 'x':
                step = min(step, k - 1)
                break
            elif x+k == R-1:
                step = min(step, k)
                break
            k += 1
    for x, y in l:
        table[x][y] = '.'
        table[x+step][y] = 'x'

R, C = map(int, input().split())
table = list(list(map(str, input())) for _ in range(R))
N = int(input())
height_l = list(map(int, input().split()))
two_dir_l = [1, -1]
dir_l = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for i, h in enumerate(height_l):
    meet, x, y = check(i, h)

    if meet:
        break_mineral(x, y)
        for i in range(4):
            nx, ny = x+dir_l[i][0], y+dir_l[i][1]
            if 0 <= nx < R and 0 <= ny < C and table[nx][ny] == 'x':
                visited = [[0] * C for _ in range(R)]
                cand = []
                recur = True
                dfs(nx, ny)
                if recur:
                    fall(cand)
    else:
        continue
show(table)
