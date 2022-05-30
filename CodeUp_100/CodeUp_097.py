Go = []
for i in range(19):
    Go_line = list(map(int, input().split()))
    Go.append(Go_line)

flip = int(input())
for i in range(flip):
    x, y = map(int, input().split())
    for m in range(19):
        Go[x-1][m] = int(not(Go[x-1][m]))
        Go[m][y-1] = int(not(Go[m][y-1]))

for i in range(len(Go)):
    for j in range(len(Go[i])):
        if j != 19-1:
            print(Go[i][j], end=' ')
        else:
            print(Go[i][j], end = '\n')
