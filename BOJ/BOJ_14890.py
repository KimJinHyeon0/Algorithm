# 경사로

N, L = map(int, input().split())
table = list(list(map(int, input().split())) for _ in range(N))
result = 0

# row
for i in range(N):
    tmp_l = 0
    tmp_h = 0
    valid = True
    j = 0
    while valid and j < N:

        if tmp_h == 0:
            tmp_h = table[i][j]
            tmp_l = 1
            j += 1
            continue

        if table[i][j] == tmp_h:
            tmp_l += 1
            j += 1
            continue

        else:  # not same height
            if table[i][j] - tmp_h == 1:  # bigger h
                if tmp_l >= L:
                    tmp_l = 1
                    tmp_h = table[i][j]
                else:
                    valid = False
                j += 1

            elif table[i][j] - tmp_h == -1 and j+L <= N:  # smaller h
                for k in range(j, j+L):
                    if table[i][k] != table[i][j]:
                        # print(f'not equal : {i, j} <-> {i, k}')
                        valid = False
                        break

                else:
                    # print(f'down success : {i}, {i, j} -> {i, k}')
                    tmp_l = 0
                    tmp_h = table[i][j+L-1]
                    j += L
            else:
                valid = False
    if valid:
        # print(f'success : {i}')
        result += 1

# print('-'*20)
# column
for i in range(N):
    tmp_l = 0
    tmp_h = 0
    valid = True
    j = 0
    while valid and j < N:
        if tmp_h == 0:
            tmp_h = table[j][i]
            tmp_l = 1
            j += 1
            continue
        if table[j][i] == tmp_h:
            tmp_l += 1
            j += 1
            continue
        else:  # not same height
            if table[j][i] - tmp_h == 1:  # bigger h
                if tmp_l >= L:
                    tmp_l = 1
                    tmp_h = table[j][i]
                else:
                    valid = False
                j += 1

            elif table[j][i] - tmp_h == -1 and j+L <= N:  # smaller h
                for k in range(j, j+L):
                    if table[k][i] != table[j][i]:
                        # print(f'not equal : {j, i} <-> {k, i}')
                        valid = False
                        break

                else:
                    # print(f'down success : {i}, {j, i} -> {k, i}')
                    tmp_l = 0
                    tmp_h = table[j+L-1][i]
                    j += L
            else:
                valid = False
    if valid:
        # print(f'success : {i}')
        result += 1





print(result)