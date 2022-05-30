def add():
    temp = cage[-1]
    min_fish = [[100], 10000] #(index, #fish)
    for i, c in enumerate(temp):
        if min_fish[1] > c:
            min_fish = [[i], c]
        elif min_fish[1] == c:
            min_fish[0].append(i)
    for index in min_fish[0]:
        cage[-1][index] = min_fish[1]+1

def stack():
    start_i, end_i, cnt = 0, 1, 3
    while cnt//2 + 1 <= N - end_i:
        for i in range((end_i - start_i)):
            for j in range(cnt//2):
                cage[-(2 + i)][end_i + j] = cage[-1-j][end_i - i - 1]
                cage[-1-j][end_i - i - 1] = 0

        start_i = end_i
        end_i += cnt//2
        cnt += 1
    return start_i

def calib(start):

    fish_dict = {}
    for i in range(start, N):
        for j in range(-1, -N, -1):
            if cage[j][i]:
                if (j, i) not in fish_dict:
                    fish_dict[(j, i)] = 0

                for k in range(2):
                    new_j, new_i = j+dir_l[k][0], i+dir_l[k][1]
                    if -N <= new_j <= -1 and 0 <= new_i < N and cage[new_j][new_i] != 0:
                        d = int((cage[j][i] - cage[new_j][new_i]) / 5)
                        if (new_j, new_i) not in fish_dict:
                            fish_dict[(new_j, new_i)] = 0
                        fish_dict[(new_j, new_i)] += d
                        fish_dict[(j, i)] -= d
            else:
                break

    for i in range(start, N):
        for j in range(-1, -N, -1):
            if cage[j][i] != 0:
                cage[j][i] += fish_dict[(j, i)]

def reindex(start):
    temp = []
    for i in range(start, N):
        for j in range(-1, -N, -1):
            if cage[j][i]:
                temp.append(cage[j][i])
            else:
                break
    new_cage = [[0] * N for _ in range(N)]
    new_cage[-1] = temp
    return new_cage

def half_stack():
    h = int(N/2)
    temp = cage[-1][:h]
    cage[-1][:h] = [0] * h
    temp.reverse()
    cage[-2][h:] = temp

    hh = int(h/2)
    up_temp = cage[-2][h:h + hh]
    down_temp = cage[-1][h:h + hh]
    cage[-2][h:h + hh] = [0] * hh
    cage[-1][h:h + hh] = [0] * hh
    up_temp.reverse()
    down_temp.reverse()
    cage[-4][h + hh:] = down_temp
    cage[-3][h + hh:] = up_temp

    return h+hh


N, K = map(int, input().split())
dir_l = [[-1, 0], [0, 1]]
cage = [[0] * N for _ in range(N)]
cage[-1] = list(map(int, input().split()))
print(cage)
result = 0

while True:
    add()
    last_start = stack()
    calib(last_start)
    cage = reindex(last_start)

    last_start = half_stack()
    calib(last_start)
    cage = reindex(last_start)

    result += 1

    temp = cage[-1]
    temp.sort()
    diff = temp[-1] - temp[0]
    if diff <= K:
        break
print(result)