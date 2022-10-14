# 톱니바퀴

def show(x):
    for row in x:
        print(*row)


def roll(n, d):
    if d == 1:  # clockwise
        gear_l[n] = [gear_l[n][-1]] + gear_l[n][:-1]

    elif d == -1:  # counter clockwise
        gear_l[n] = gear_l[n][1:] + [gear_l[n][0]]


def cal():
    return sum(gear_l[i][0] * (2**i) for i in range(4))


def connect_check(a, b):
    return gear_l[a][2] == gear_l[b][6]


def recur(n, d):
    left, right = True, True
    if 0 <= n-1 and not visited[n-1]:
        left = connect_check(n-1, n)

    if n+1 < 4 and not visited[n+1]:
        right = connect_check(n, n+1)

    roll(n, d)
    visited[n] = True
    if not left:
        recur(n-1, -d)
    if not right:
        recur(n+1, -d)


gear_l = list(list(map(int, input())) for _ in range(4))
K = int(input())
cycle_l = [[] for _ in range(K)]
for i in range(K):
    n, d = map(int, input().split())
    cycle_l[i] = [n-1, d]
for g, d in cycle_l:
    visited = [False] * 4
    recur(g, d)
print(cal())