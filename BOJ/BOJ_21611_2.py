from collections import deque

def ice(d, s):
    x, y = s_x, s_y
    print(d, s)
    for _ in range(s):
        x, y = x+dir_l[d][0], y+dir_l[d][1]
        if 0 <= x < N and 0 <= y < N:
            table[x][y] = 0

def explode():
    x, y = s_x, s_y
    marble_l = deque()
    pre_value = 1
    dir = -1
    for i in range(1, N):
        for j in range(2):
            dir = (dir+1)%4
            for k in range(i):
                x, y = x+circle_l[dir][0], y+circle_l[dir][1]
                print(dir)
                value = table[x][y]
                if not value*pre_value:
                    break
                if value:
                    marble_l.append(value)
                    pre_value = value
    print(marble_l)






N, M = map(int, input().split())
table = list(list(map(int, input().split())) for _ in range(N))
magic_l = list(list(map(int, input().split())) for _ in range(M))
dir_l = [[], [-1, 0], [1, 0], [0, -1], [0, 1]]
s_x, s_y = N//2, N//2
circle_l = [[0, -1], [1, 0], [0, 1], [-1, 0]]

for d, s in magic_l:
    ice(d, s)
    print(table)
    explode()
    exit()