N, Q = map(int, input().split())
table = list(list(map(int, input().split())) for _ in range(N**2 - 1))
L = list(map(int, input().split()))

for k in L:
    print(k)