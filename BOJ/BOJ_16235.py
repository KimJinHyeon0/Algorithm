N, M, K = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(N))
tree = [[[] for _ in range(N)] for _ in range(N)]
table = [[5 for _ in range(N)] for _ in range(N)]

dx_l = [-1, -1, -1, 0, 0, 1, 1, 1]
dy_l = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(M):
    x, y, age = map(int, input().split())
    tree[x-1][y-1] = [age]

for _ in range(K):
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if table[i][j] >= tree[i][j][k]:
                    table[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    table[i][j] += sum(map(lambda x: x//2, tree[i][j][k:]))
                    del tree[i][j][k:]
                    break
    for i in range(N):
        for j in range(N):
            for q in tree[i][j]: #q = age
                if q % 5 == 0:
                    for k in range(8):
                        x, y = i + dx_l[k], j + dy_l[k]
                        if 0 <= x < N and 0 <= y < N:
                            tree[x][y].insert(0, 1)
            table[i][j] += A[i][j]

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j])
print(answer)