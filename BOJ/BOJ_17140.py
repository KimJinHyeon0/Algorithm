r, c, k = map(int, input().split())
r -= 1
c -= 1
A = list(list(map(int, input().split())) for _ in range(3))
result = 0
t = 0
if A[r][c] >= k:
    print(result)
else:
    print('1')
    