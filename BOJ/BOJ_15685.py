from copy import deepcopy

def calc():
    global result
    for i in range(100):
        for j in range(100):
            nx, ny = i, j
            temp = 1
            for k in range(4):
                nx += s[k][0]
                ny += s[k][1]
                if 0 <= nx < 100 and 0 <= ny < 100:
                    temp *= table[ny][nx]
            result += temp


def mapping(k):
    x, y, step_l, cnt = dragon_l[k]
    if cnt == 0:
        return

    for i in range(len(step_l)-1, -1, -1):
        nstep = (step_l[i]+1)%4
        x, y = x + dx_l[nstep], y + dy_l[nstep]
        table[y][x] = 1
        step_l.append(nstep)

    dragon_l[k] = [x, y, step_l, cnt-1]
    mapping(k)


N = int(input())
table = [[0 for _ in range(100)] for _ in range(100)]
dragon_l = []
shit = []
for i in range(N):
    temp = list(map(int, input().split()))
    temp[2] = [temp[2]]
    dragon_l.append(temp)
    table[temp[1]][temp[0]] = 1
dx_l = [1, 0, -1, 0]
dy_l = [0, -1, 0, 1]

s = [(0, 0), (1, 0), (0, 1), (1, 1)]
result = 0

for i in range(N):
    mapping(i)
print(shit)
calc()
print(result)
