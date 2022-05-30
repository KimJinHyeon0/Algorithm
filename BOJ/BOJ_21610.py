def move(d, s):
    for i in range(len(cloud)):
        for j in range(s):
            cloud[i][0] = (cloud[i][0] + dir_l[d][0])%N
            cloud[i][1] = (cloud[i][1] + dir_l[d][1])%N

def pour():
    for i in range(len(cloud)):
        table[cloud[i][0]][cloud[i][1]] += 1

def water_magic():
    for x, y in cloud:
        cnt = 0
        for i in range(4):
            nx, ny = x+water_dir[i][0], y+water_dir[i][1]
            if 0 <= nx < N and 0 <= ny < N and table[nx][ny]:
                cnt += 1
        table[x][y] += cnt

def over2(type):
    global result
    new_cloud = []
    for i in range(N):
        for j in range(N):
            if type:
                result += table[i][j]

            if table[i][j] >= 2 and [i, j] not in cloud:
                new_cloud.append([i, j])
                table[i][j] -= 2
    if type:
        result -= 2*len(new_cloud)
    return new_cloud

N, M = map(int, input().split())
table = list(list(map(int, input().split())) for _ in range(N))
magic = list(list(map(int, input().split())) for _ in range(M))
dir_l = [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
water_dir = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
result = 0
for p, [d, s] in enumerate(magic):
    move(d, s)
    pour()
    water_magic()
    if p == len(magic) - 1:
        cloud = over2(1)
    else:
        cloud = over2(0)

print(result)