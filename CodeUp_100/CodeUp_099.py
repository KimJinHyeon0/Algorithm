stage = []
for i in range(10):
    stage_line = list(map(int, input().split()))
    stage.append(stage_line)
i, j = 1, 1

while True:
    if stage[i][j] == 2:
        stage[i][j] = 9
        break
    elif stage[i][j+1] ==1:
        if stage[i+1][j] ==1:
            stage[i][j] = 9
            break
        else:
            stage[i][j] = 9
            i += 1
    elif i == 8 and j == 8:
        break
    else:
        stage[i][j] = 9
        j += 1



for i in range(len(stage)):
    for j in range(len(stage[i])):
        if j != 10-1:
            print(stage[i][j], end=' ')
        else:
            print(stage[i][j], end='\n')
