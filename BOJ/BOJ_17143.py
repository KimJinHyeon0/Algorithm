R, C, M = map(int, input().split())
table = [[0] * C for _ in range(R)]

shark_l = dict()
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    table[r-1][c-1] = z
    shark_l[z] = [r-1, c-1, s, d]
dir_l = [[], [-1, 0], [1, 0], [0, 1], [0, -1]]

result = 0

for i in range(C):
    tmp = [[0] * C for _ in range(R)]
    for j in range(R):
        target = table[j][i]
        if target:
            table[j][i] = 0
            result += target
            del shark_l[target]
            break

    for z, r, c, s, d in zip(shark_l.keys(), shark_l.values()):
        n_r, n_c = r + s*(dir_l[d][0]), c + s*(dir_l[d][1])
        n_d = d

        recur = True
        while recur:
            recur = False
            if 0 > n_r:
                n_r *= -1
                n_d = 2
                recur = True
            if n_r > R-1:
                n_r = R-n_r
                n_d = 1
                recur = True

            if 0 > n_c:
                n_c *= -1
                n_d = 3
                recur = True

            if n_r > R-1:
                n_r = C-n_r
                n_d = 4
                recur = True


        if tmp[n_r][n_c]:
            if tmp[n_r][n_c] < z:
                tmp[n_r][n_c] = z
                del shark_l[tmp[n_r][n_c]]
            else:
                del shark_l[z]
        else:
            tmp[n_r][n_c] = z
    table = tmp
print(result)
