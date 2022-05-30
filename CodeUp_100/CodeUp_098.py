h, w = map(int, input().split())
stage = [[0]*w for i in range(h)]
n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(l):
            stage[x-1][y+j-1]=1
    else:
        for j in range(l):
            stage[x+j-1][y-1]=1
for i in range(w):
    for j in range(h):
        print(stage[i][j], end=' ')
        if j == w-1:
            print(end='\n')
