N, S = map(int, input().split())
A = list(map(int, input().split()))

result = 1e6
i, j, temp = 0, 0, A[0]
while i < N and j < N:
    if temp < S:
        j += 1
        if j < N:
            temp += A[j]
    else:
        result = min(result, j-i+1)
        temp -= A[i]
        i += 1
if result == 1e6:
    result = 0
print(result)