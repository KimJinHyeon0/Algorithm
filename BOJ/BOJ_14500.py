N, M = map(int, input().split())
table = list(list(map(int, input().split())) for _ in range(N))
dir_l = [[0, 0],
         [-1, 0], [0, -1], [1, 0], [0, 1],
         [-1, 1], [-1, -1], [1, -1], [1, 1]]

tetromino_l = [[0, 1, 1, 1], [0, 2, 2, 2], #1
               [0, 3, 4, 1], #2
               [0, 3, 3, 4], [0, 4, 4, 1], [0, 1, 1, 2], [0, 2, 2, 3], #3_1
               [0, 3, 3, 2], [0, 4, 4, 3], [0, 1, 1, 4], [0, 2, 2, 1], #3_2
               [0, 3, 4, 3], [0, 4, 1, 4], [0, 1, 2, 1], [0, 2, 3, 2], #4_1
               [0, 3, 2, 3], [0, 4, 3, 4], [0, 1, 4, 1], [0, 2, 1, 2], #4_2
               [0, 4, 3, 5], [0, 1, 4, 6], [0, 2, 1, 7], [0, 3, 2, 8]] #5_1

result = 0
for x in range(N):
    for y in range(M):
        for k in tetromino_l:
            tmp = 0
            nx, ny = x, y
            for i in range(4):
                nx, ny = nx+ dir_l[k[i]][0], ny + dir_l[k[i]][1]
                if 0 <= nx < N and 0 <= ny < M:
                    tmp += table[nx][ny]
                else:
                    break
            else:
                result = max(result, tmp)
print(result)