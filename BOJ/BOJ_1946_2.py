import sys

input = lambda : sys.stdin.readline()

T = int(input())

for i in range(T):
    N = int(input())
    candidate = sorted([list(map(int, input().split())) for _ in range(N)])

    cnt = 1
    min = candidate[0][1]

    for i in range(1, N):
        if candidate[i][1] < min:
            cnt += 1
            min = candidate[i][1]

    print(cnt)
