import sys
input = lambda: sys.stdin.readline()

N, K = map(int, input().split())

data = [[0,0] for _ in range(N)]

for i in range(N):
    data[i][0], data[i][1] = map(int, input().split())

temp = [0,0] #무게 합, value 합
result = [0,0] #무게 합, value 합

for i in range(N):
    if data[i][0] < K:
        temp[0], temp[1] = data[i][0], data[i][1]
    for j in range(N):
        if i == j:
            continue
        if temp[0] + data[j][0] <= K:
            temp[0] += data[j][0]
            temp[1] += data[j][1]
    if result[1] < temp[1]:
        result[0], result[1] = temp[0], temp[1]
    temp = [0,0]

print(result[1])