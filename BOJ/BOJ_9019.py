from collections import deque

def dslr(i, x):
    if i == 'D':
        return (x * 2) % 10000
    elif i == 'S':
        return 9999 if x == 0 else x-1
    elif i == 'L': # 1234
        m = x // 1000 #1
        n = x % 1000 #234
        return 10*n + m #2341
    else: #'R'
        m = x // 10
        n = x % 10
        return 1000*n + m

def bfs():
    q = deque()
    q.append([A, '']) # '' == result
    while q:
        num, result = q.popleft()
        for case in ['D', 'S', 'L', 'R']:
            new = dslr(case, num)
            if new == B:
                return result + case
            elif not visited[new]:
                visited[new] = True
                q.append([new, result + case])

for i in range(int(input())):
    A, B = map(int, input().split())
    visited = [False] * 10000
    print(bfs())
