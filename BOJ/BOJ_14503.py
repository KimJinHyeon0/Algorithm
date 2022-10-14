# 로봇 청소기

def show(x):
    for row in x:
        print(*row)

def clean():
    global r, c, cleaned

    table[r][c] = -1
    cleaned += 1

def turn_left():
    global d

    d = (d+3)%4

def is_valid():
    global r, c, d

    nr, nc = r+dir_l[d][0], c+dir_l[d][1]

    if 0 <= nr < N and 0 <= nc < M and not table[nr][nc]:
        r, c = nr, nc
        clean()
        return True
    else:
        return False

def back():
    global r, c, d, recur

    nr, nc = r+dir_l[d-2][0], c+dir_l[d-2][1]
    if 0 <= nr < N and 0 <= nc < M and table[nr][nc] != 1:
        r, c = nr, nc
        recur = True
    else:
        recur = False

N, M = map(int, input().split())
dir_l = [[-1, 0], [0, 1], [1, 0], [0, -1]]
r, c, d = map(int, input().split())

table = list(list(map(int, input().split())) for _ in range(N))
cleaned = 0

recur = True
clean()
while recur:
    for i in range(4):
        turn_left()
        if is_valid():
            break
    else:
        back()
print(cleaned)


