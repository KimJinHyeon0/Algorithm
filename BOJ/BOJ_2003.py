N, M = map(int, input().split())
A = list(map(int, input().split()))
result = 0

i, j, temp = 0, 0, A[0]
while i < N and j < N:
    if temp > M:
        temp -= A[i]
        i += 1
    elif temp < M:
        j += 1
        if j < N:
            temp += A[j]
    else:
        result += 1
        j += 1
        if j < N:
            temp += A[j]

print(result)