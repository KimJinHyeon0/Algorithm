Go = [[0]*19 for i in range(19)]
    
num = int(input())

for i in range(num):
    x, y = map(int, input().split())
    Go[x-1][y-1] = 1
    
for i in range(len(Go)):
    for j in range(len(Go[i])):
        if j != 18:
            print(Go[i][j],end=' ')
        else:
            print(Go[i][j], end = '\n')
