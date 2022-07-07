N, M = map(int, input().split())
A = list(list(map(int, input())) for _ in range(N))
B = list(list(map(int, input())) for _ in range(N))

window = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

def check():
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return False
    return True


def cal():
    cnt = 0
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                for case in window:
                    nx, ny = i+case[0], j+case[1]
                    A[nx][ny] = abs(A[nx][ny] - 1)
                cnt += 1

    if check():
        return cnt
    else:
        return -1

if check():
    print(0)
else:
    if N < 3 or M < 3:
        print(-1)
    else:
        print(cal())
