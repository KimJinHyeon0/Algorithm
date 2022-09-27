from collections import deque

def bfs():
    q = deque()
    x, y = min(A, B, C), max(A, B, C)
    q.append((x, y))
    check[x][y] = True
    while q:
        x, y = q.popleft()
        z = D-x-y
        if x == y == z:
            return 1
        for a, b in (x, y), (x, z), (y, z):
            if a < b:
                b -= a
                a *= 2
            elif a > b:
                a -= b
                b *= 2
            else:
                continue
            c = D-a-b
            X = min(a, b, c)
            Y = max(a, b, c)
            if not check[X][Y]:
                q.append((X, Y))
                check[X][Y] = True
    return 0

A, B, C = map(int, input().split())
D = A+B+C
check = [[False]*D for _ in range(D)]
if D % 3:
    print(0)
else:
    print(bfs())
